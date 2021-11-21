from flask import Blueprint

profile = Blueprint('profile', __name__)

@profile.route('/')
def timeline():
    # Do some stuff
    return 'profile'

@profile.route('/photos')
def photos():
    # Do some stuff
    return 'profile/photos'

@profile.route('/about')
def about():
    # Do some stuff
    return 'profile/about'