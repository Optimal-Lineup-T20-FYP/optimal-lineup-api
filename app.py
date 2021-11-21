from flask import Flask
import pandas as pd

from routes.profile import profile

app = Flask(__name__)
app.register_blueprint(profile, url_prefix='/profile')

@app.route('/')
def hello():
    return "Hello World!"
    