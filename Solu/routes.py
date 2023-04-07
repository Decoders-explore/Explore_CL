import os
import secrets
from logging import debug
from flask import request,render_template,url_for,redirect,request,abort,Response
from Solu import app

import numpy as np

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',title="Fungo",home="active")


    
       
