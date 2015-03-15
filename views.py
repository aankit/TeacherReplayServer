from hello import app
import subprocess

@app.route('/')
@app.route('/index')
def index():
    return "Building Flask From Scratch!"

@app.route('/cam/<state>')
def cam(state):
    if state == 'on':
        cmd = ["sudo", "touch", "/home/pi/hooks/start_record"]
        p = subprocess.Popen(cmd, stdout = subprocess.PIPE, stderr = subprocess.PIPE, stdin = subprocess.PIPE)
        out, err = p.communicate()
        return out
    elif state == 'off':
        cmd = ["sudo", "touch", "/home/pi/hooks/stop_record"]
        p = subprocess.Popen(cmd, stdout = subprocess.PIPE, stderr = subprocess.PIPE, stdin = subprocess.PIPE)
        out, err = p.communicate()
        return out
    else:
        return state
