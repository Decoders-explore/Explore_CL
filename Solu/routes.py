import os
import secrets
from logging import debug
from flask import request,render_template,url_for,redirect,request,abort,Response
from Solu import app

from Solu.utils import access_camera
import numpy as np

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',title="Fungo",home="active")

@app.route("/meetourteam")
def meetour():
    return render_template("meetourteam.html")
@app.route("/measures")
def measures():
    return render_template("intro.html")

@app.route('/inference')    
def inference():
    return render_template('RealTimeInference.html')

@app.route('/videofeed')
def videofeed():
    return Response(access_camera.gen_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')