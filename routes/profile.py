from flask import Blueprint, jsonify
from models import statistics

from bing_image_downloader import downloader

profile = Blueprint('profile', __name__)

@profile.route('/all')
def all():
    players = list(set(statistics.getAllBattersName()) | set(statistics.getAllBowlersName()))
    return jsonify(players=players)

@profile.route('/<player_name>')
def player_data(player_name):
    results = statistics.getPlayerData(player_name)
    if(results == {}):
        return "Player Not Found"
    try:
        downloader.download(player_name + " cricket player", limit=1, adult_filter_off=True, output_dir='static', force_replace=False, timeout=60, verbose=False)
        results['image'] = True
    except:
        results['image'] = False
    return jsonify(results=results)
