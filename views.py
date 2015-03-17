from replay import app
from replaydb.database import db_session
from replaydb.database import *
from flask import render_template
import subprocess
import os

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname' : 'Teacher'}
    navigation = {'Set Goals': '/goals',
            'View Replays': '/replays',
            'Save Evidence': '/evidence',
            'Schedule' :'/schedule',
            'Sharing': '/sharing'
            }
    return render_template('index.html',
            title='Home',
            user=user,
            navigation=navigation)

#@app.route('/login', methods=['GET', 'POST'])
#def login():
#    if request.method = 'POST':
#        return 'No login function yet.'
#    else:
#        return 'No login page yet.'

@app.route('/schedule', methods=['GET', 'POST'])
def schedule():
    return 'schedule page'

@app.route('/replays')
def replays():
    video_path = '/var/www/replay/videos'
    list_of_videos = os.listdir(video_path)
    videos = dict(zip(list_of_videos, ["/videos/%s" %(vid) for vid in list_of_videos]))
    return render_template('videos.html', title='Videos', list_of_videos=videos)
