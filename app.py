from flask import Flask
from flask_cors import CORS

from routes.profile import profile

app = Flask(__name__)
CORS(app)
app.register_blueprint(profile, url_prefix='/profile')

@app.route('/')
def hello():
    return "Hello World!"
    