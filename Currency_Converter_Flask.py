#Commands to run app on powershell
#> $env:FLASK_APP = "hello"
#> flask run
#or   flask run --host=0.0.0.0   to be open
#to enable debugger set the FLASK_ENV environment variable to "development" before run

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "curren "
    