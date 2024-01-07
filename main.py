from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from PIL import Image
import os
import base64
app = Flask(__name__)
 
upload_folder = os.path.join('static', 'uploads')
  
@app.route('/', methods=['GET', 'POST'])#https://geekpython.in/render-images-from-flask
def homepage():
    if request.method == 'POST':
        file = request.files['img']
        image_string = base64.b64encode(file.read())
        return render_template('base.html', img = image_string)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
    return render_template('base.html')

if __name__ == '__main__':
    app.run(debug=True, port=8001)