import os
import subprocess
from flask import Flask, jsonify, request
import stat

app = Flask(__name__)
# setting environment variable
os.environ['TOKEN'] = 'TESTAPP'
# making bash file executable
bash_file = 'app/deploy.sh'
file_stats = os.stat(bash_file)
os.chmod(bash_file, file_stats.st_mode | stat.S_IEXEC)


@app.route('/')
def index():
    return 'Docker-Travis hook listener'


@app.route('/ping', methods=['GET', 'POST'])
def pong():
    if request.method == 'POST':
        args = request.args
        token = args.get('token')
        print('req token: ' + token)
        if str(token) == str(os.environ.get('TOKEN')):
            subprocess.call(bash_file)
            return jsonify(success=True)
        return jsonify(success=False), 500
    if request.method == 'GET':
        return "pong!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
