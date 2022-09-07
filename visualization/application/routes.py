from application import app
from flask import render_template
import pandas as pd
import json
import plotly
import plotly.express as px
import os

IMAGE_FOLDER= os.path.join('static', 'images')
app.config['UPLOAD_FOLDER']=IMAGE_FOLDER


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chart1')
def chart1():

    

    # Graph One
    graph1 = os.path.join(app.config['IMAGE_FOLDER'], 'fig1.png')

    # Graph two
    
    graph2 = os.path.join(app.config['IMAGE_FOLDER'], 'fig2.png')


    # Graph three
    
    graph3 = os.path.join(app.config['IMAGE_FOLDER'], 'fig3.png')

    # Graph four
    graph4 = os.path.join(app.config['IMAGE_FOLDER'], 'fig4.png')

    return render_template('index.html', user_image=graph1)

