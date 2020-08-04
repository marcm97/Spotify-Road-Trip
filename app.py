import os
from flask import Flask, session, request, redirect, render_template, jsonify
from flask_session import Session
import pandas as pd
import spotipy
import uuid

from utils.generate_playlist import create_playlist
from utils.generate_playlist import add_songs

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(64)
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_FILE_DIR'] = './.flask_session/'
Session(app)

caches_folder = './.spotify_caches/'
if not os.path.exists(caches_folder):
    os.makedirs(caches_folder)

def session_cache_path():
    return caches_folder + session.get('uuid')

@app.route('/')
def index():
    if not session.get('uuid'):
        # Step 1. Visitor is unknown, give random ID
        session['uuid'] = str(uuid.uuid4())

    auth_manager = spotipy.oauth2.SpotifyOAuth(scope='user-read-currently-playing playlist-modify-private user-library-read playlist-modify-public playlist-read-private',
                                                cache_path=session_cache_path(),
                                                show_dialog=True)

    if request.args.get("code"):
        # Step 3. Being redirected from Spotify auth page
        auth_manager.get_access_token(request.args.get("code"))
        return redirect('/')

    if not auth_manager.get_cached_token():
        # Step 2. Display sign in link when no token
        auth_url = auth_manager.get_authorize_url()
        return render_template('login.html', signin_url=auth_url)

    # Step 4. Signed in, display data
    spotify = spotipy.Spotify(auth_manager=auth_manager)
    post = {
        "username": spotify.me()["display_name"],
        "sign_out": '/sign_out',
        "generate_playlist": '/generate_playlist'
    }
    return render_template('home.html', posts=post)

@app.route('/sign_out')
def sign_out():
    os.remove(session_cache_path())
    try:
        # Remove the CACHE file (.cache-test) so that a new user can authorize.
        os.remove(session_cache_path())
    except OSError as e:
        print ("Error: %s - %s." % (e.filename, e.strerror))
    session.clear()
    return redirect('/')

@app.route('/generate_playlist', methods=['POST'])
def generate_playlist():
    # Gets data from the home page
    data = request.get_json()
    playlist_name=data["playlist_name"]
    origin =data["origin"]
    destination = data["destination"]
    print("Ok this is a post method \n" +  playlist_name + "\n" + origin + "\n" + destination)
    return f"<h2>HTML Ok this is a post method {origin} {destination}</h2>"\

'''
Following lines allow application to be run more conveniently with
`python app.py` (Make sure you're using python3)
(Also includes directive to leverage pythons threading capacity.)
'''
if __name__ == '__main__':
	app.run(threaded=True, port=int(os.environ.get("PORT", 8080)))
