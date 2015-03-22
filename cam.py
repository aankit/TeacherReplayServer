from replay import app
from replaydb.database import db_session
from replaydb.database import *
from flask import render_template
import subprocess

#@app.route('/')
#@app.route('/index')
#def index():
#    return "Welcome to Teacher Replay!"

#@app.route('/login', methods=['GET', 'POST'])
#def login():
#    if request.method = 'POST':
#        return 'No login function yet.'
#    else:
#        return 'No login page yet.'

@app.route('/record/<state>')
def record(state):
    return_text = ""
    if state == 'on':
        cam = subprocess.call(["sudo", "service", "picam", "start"])
        if cam == 0:
            return_text += "cam on:"
            record = subprocess.call(["touch", "/home/pi/hooks/start_record"])
            if record == 0:
                return return_text + "we are now recording video and audio!"
    elif state == 'off':
        record = subprocess.call(["touch", "/home/pi/hooks/stop_record"])
        if record == 0:
            cam = subprocess.call(["sudo", "service", "picam", "stop"])
            if cam == 0:
                return "successfully shutdown"
    else:
        return "Please either send on or off. Thanks, your friendly neighborhood API."

@app.route('/cam/<state>')
def cam(state):
    if state == 'on':
        cmd = ["sudo", "service", "picam", "start"]
        p = subprocess.Popen(cmd, stdout = subprocess.PIPE, stderr = subprocess.PIPE, stdin = subprocess.PIPE)
        out, err = p.communicate()
        return out
    elif state == 'off':
        cmd = ["sudo", "service", "picam", "stop"]
        p = subprocess.Popen(cmd, stdout = subprocess.PIPE, stderr = subprocess.PIPE, stdin = subprocess.PIPE)
        out, err = p.communicate()
        return out
    else:
        return "Please either send on or off. Thanks, your friendly neighborhood API."

#@app.route('/schedule', methods=['GET', 'POST'])
#def schedule():
#    return 'schedule page'

@app.route('/marker/<timestamp>/<mode>')
def marker(timestamp, mode):
    #mode_obj = Mode(mode)
    return '%s with %s mode' %(timestamp, mode)


