from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/', methods=['GET',"POST"])
def index():
    return render_template("base.html",title="test")


app.run(host='0.0.0.0', port=81)
