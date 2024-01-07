from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from PIL import Image
import os
import base64
app = Flask(__name__)
 
upload_folder = os.path.join('static', 'uploads')
 
app.config['UPLOAD'] = upload_folder
 
@app.route('/', methods=['GET', 'POST'])#https://geekpython.in/render-images-from-flask
def homepage():
    return render_template("base.html")
@app.route('/result', methods=['POST'])
def upload_file():
    file = request.files['img']
    image_string = base64.b64encode(file.read())
    return render_template('base.html', img = image_string)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          

if __name__ == '__main__':
    app.run(debug=True, port=8001)