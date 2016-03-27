import os
import subprocess
from flask import Flask, jsonify, request, session
from flask.ext.session import Session
import stat

app = Flask(__name__)
# Session Configs
SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
Session(app)
# setting environment variable
os.environ['TOKEN'] = 'TESTAPP'
# making bash file executable
bash_file = 'app/deploy.sh'
file_stats = os.stat(bash_file)
os.chmod(bash_file, file_stats.st_mode | stat.S_IEXEC)

# initialise session variables
session['docker'] = 0
session['travis'] = 1   # for travis status 1 means failure


def run_bash():
    # reset session variables
    session['docker'] = 0
    session['travis'] = 1
    # run bash
    subprocess.call(bash_file)


def state():
    return {'travis': session['travis'], 'docker': session['docker']}


@app.route('/')
def index():
    # store session
    return 'Docker-Travis hook listener'


@app.route('/travis', methods=['POST'])
def travis():
    # set travis session
    args = request.args
    print(args)
    # successful build has a status of 0
    session['travis'] = args.status
    # check if docker session is set
    docker = session['docker']
    if docker == 1 and session['travis'] == 0:
        run_bash()
    return jsonify(state())


@app.route('/docker-travis', methods=['POST'])
def docker_travis():
    args = request.args
    token = args.get('token')
    travis = session['travis']
    # print('req token: ' + token)
    if str(token) == str(os.environ.get('TOKEN')) and travis == 0:
        run_bash()
    return jsonify(state()), 500


@app.route('/docker', methods=['POST'])
def docker():
    args = request.args
    token = args.get('token')
    print('req token: ' + token)
    if str(token) == str(os.environ.get('TOKEN')):
        subprocess.call(bash_file)
        return jsonify(success=True)
    return jsonify(success=False), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
