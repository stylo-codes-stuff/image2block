from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from PIL import Image
import os
import glob
app = Flask(__name__)
 
upload_folder = os.path.join('static', 'uploads')
 
app.config['UPLOAD'] = upload_folder
 
@app.route('/', methods=['GET', 'POST'])#https://geekpython.in/render-images-from-flask
def upload_file():
    for file in os.listdir("static/uploads"):
        os.remove(file)
    if request.method == 'POST':

        file = request.files['img']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD'], filename))
        img = os.path.join(app.config['UPLOAD'], filename)
        image = Image.open(img).convert('RGB')
        image = image.resize((500, 500))
        image.save(os.path.join(app.config['UPLOAD'], filename))
        return render_template('base.html', img=img)
    return render_template('base.html')
 
 
if __name__ == '__main__':
    app.run(debug=True, port=8001)