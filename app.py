import os
from flask import Flask, session, request, redirect, render_template, jsonify
from flask_session import Session
import pandas as pd
import spotipy
import uuid

from generate_playlist import create_playlist
from generate_playlist import add_songs

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
        "playlists": '/playlists',
        "generate_playlist": '/generate_playlist',
        "currently_playing": '/currently_playing',
        "current_user": '/current_user'
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


@app.route('/playlists')
def playlists():
    auth_manager = spotipy.oauth2.SpotifyOAuth(cache_path=session_cache_path())
    if not auth_manager.get_cached_token():
        return redirect('/')

    spotify = spotipy.Spotify(auth_manager=auth_manager)
    return spotify.current_user_playlists()


@app.route('/generate_playlist', methods=['POST'])
def generate_playlist():
    data = request.get_json()
    playlist_name=data["playlist_name"]
    origin =data["origin"]
    destination = data["destination"]
    print("Ok this is a post method \n" +  playlist_name + "\n" + origin + "\n" + destination)
    return f"<h2>HTML Ok this is a post method {origin} {destination}</h2>"\

    '''
    auth_manager = spotipy.oauth2.SpotifyOAuth(cache_path=session_cache_path())
    if not auth_manager.get_cached_token():
        return redirect('/')
    
    spotify = spotipy.Spotify(auth_manager=auth_manager)
    
    username = spotify.current_user()['id']
    playlist_id = create_playlist("newYork", spotify, username)  # TODO: Allow user to input
    duration = 30 * 60 * 1000  # TODO: Get time from google map
    states = ["New York"]  # TODO: Return states from google map
    # TODO: weight towards destination state/cities

    count = len(states)
    for state in states:
        songs = pd.read_csv("./final_datasets/" + state + ".csv")  # TODO: read from github instead of local
        songs = songs[songs["uris"] != "error"]
        songs = songs[songs["popularity"] != "0"]
        add_songs(playlist_id, songs, duration / count, spotify, username)
  
    return jsonify(spotify.playlist(playlist_id))
   
    return origin + ' ' + destination
    '''

@app.route('/currently_playing')
def currently_playing():
    auth_manager = spotipy.oauth2.SpotifyOAuth(cache_path=session_cache_path())
    if not auth_manager.get_cached_token():
        return redirect('/')
    spotify = spotipy.Spotify(auth_manager=auth_manager)
    track = spotify.current_user_playing_track()
    if not track is None:
        return track
    return "No track currently playing."


@app.route('/current_user')
def current_user():
    auth_manager = spotipy.oauth2.SpotifyOAuth(cache_path=session_cache_path())
    if not auth_manager.get_cached_token():
        return redirect('/')
    spotify = spotipy.Spotify(auth_manager=auth_manager)
    return jsonify(spotify.current_user())


'''
Following lines allow application to be run more conveniently with
`python app.py` (Make sure you're using python3)
(Also includes directive to leverage pythons threading capacity.)
'''
if __name__ == '__main__':
	app.run(threaded=True, port=int(os.environ.get("PORT", 8080)))
