from flask import Flask, render_template, url_for, request, redirect
from caption import *
import warnings
import base64
import random
warnings.filterwarnings("ignore")



app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('camera.html')





@app.route("/", methods=['GET', 'POST'])
def getimg():
    if request.method == 'POST':
        img = request.form['link']


        img = base64.b64decode(img)
        convert_and_save(img)
        
        caption = caption_this_image("static/imageToSave.png")

        result_dic = {
			'image':"static/imageToSave.png",
			'description' : caption
		}

    #return render_template('camera.html')
    return render_template('camera.html', results = result_dic)
    
def convert_and_save(b64_string):
    with open("static/imageToSave.png", "wb") as fh:
        fh.write(b64_string)


if __name__ == '__main__':
	app.run(debug = True)