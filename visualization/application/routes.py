from application import app
from flask import render_template
import pandas as pd
import json
import plotly
import plotly.express as px
import os
from flask import request
import sys
import webbrowser
import logging


IMAGE_FOLDER= os.path.join('static', 'images')
DATA_FOLDER=os.path.join("/home/stella/Documents/Interviews/mpesa2/Mpesa-analysis/data/")
app.config['UPLOAD_FOLDER']=IMAGE_FOLDER
app.config['DATA_FOLDER']=DATA_FOLDER



@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')


@app.route('/attachment')
def getattachment():
    
    oldurl = os.system('python3 getAttachment.py')
    logging.info({oldurl})
    
    url= os.popen('cat',oldurl).read()
    webbrowser.open( str(url),new=0, autoraise=True)
    return  
    
        

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

@app.route('/upload')  
def upload():  
    return render_template("file_upload_form.html")  
 
@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        f = request.files['file']  
        
        f.save(DATA_FOLDER+f.filename)  
        return render_template("success.html", name = f.filename) 

 
  
if __name__ == '__main__':  
    app.run(debug = True)  
