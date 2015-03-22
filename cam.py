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
    if state == 'on':
        try:
            subprocess.call("/var/www/replay/shell_scripts/cam_on.sh")
        except:
            return "we are not recording"
        return "its on"
    elif state == 'off':
        try:
            subprocess.call("/var/www/replay/shell_scripts/cam_off.sh")
        except:
            return "we are stiiiil recording"
        return "its off"
    else:
        return "Please either send on or off. Thanks, your friendly neighborhood API."

#@app.route('/cam/<state>')
#def cam(state):
#    if state == 'on':
#        cmd = ["sudo", "service", "picam", "start"]
#        p = subprocess.Popen(cmd, stdout = subprocess.PIPE, stderr = subprocess.PIPE, stdin = subprocess.PIPE)
#        out, err = p.communicate()
#        return out
#    elif state == 'off':
#        cmd = ["sudo", "service", "picam", "stop"]
#        p = subprocess.Popen(cmd, stdout = subprocess.PIPE, stderr = subprocess.PIPE, stdin = subprocess.PIPE)
#        out, err = p.communicate()
#        return out
#    else:
#        return "Please either send on or off. Thanks, your friendly neighborhood API."

#@app.route('/schedule', methods=['GET', 'POST'])
#def schedule():
#    return 'schedule page'

#@app.route('/marker/<timestamp>/<mode>')
#def marker(timestamp, mode):
#    #mode_obj = Mode(mode)
#    return '%s with %s mode' %(timestamp, mode)


