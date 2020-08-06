import pandas as pd
import os

from utils.route import states_along_route
from utils.route import trip_duration_seconds

def search_playlist(sp, username, new_playlist):
    playListID = ""
    playlists = sp.user_playlists(username)
    for playlist in playlists["items"]:
        if (playlist["name"] == new_playlist):
            playListID = playlist["id"]
    return playListID


def create_playlist(playlist_name, sp, username):
    # See if playlist already exists
    # if exists, return playlist id 
    # else create new one
    playListID = search_playlist(sp, username, playlist_name)

    if (playListID == ""):
        sp.user_playlist_create(username, playlist_name, public=True)
        playListID = search_playlist(sp, username, playlist_name)
        return (playListID, True)
    return (playListID, False)


def add_songs(playListID, songs, duration, sp, username):
    # TODO: filter songs based on features/analysis
    # Endpoint analysis: danceability, loudness, energy, valence, tempo
    # Endpoint 'get track': release date (album), popularity, uri, explicit, genres
    # Filter from Spotify playlists?
    # Look into sliders? radar charts?
    song_set = set()
    count=0
    while duration > 0:  # TODO: add condition if duration < 0 (hack: stop early if duration doesn't change)
        k = 4  # bias towards more popular songs by taking popularity to k power
        bag = songs.sample(weights=[int(x)**k if str(x).isdigit() else 0 for x in songs.popularity])
        if count>10:
            duration=0
        if bag.iloc[0, -5] not in song_set:
            song_set.add(bag.iloc[0, -5])
            uri = bag.iloc[0, -4]  # TODO: change to column name later
            song_length = int(bag.iloc[0, -3])
            try:
                sp.user_playlist_add_tracks(username, playlist_id=playListID, tracks=[uri], position=None)
                duration = duration - song_length
            except:
                pass

        else:
            count+=1

def make_roadtrip_playlist(origin, destination, playlist_id, sp, username):
    duration = trip_duration_seconds(origin, destination) * 1000 
    states = list(states_along_route(origin, destination).keys())  # TODO: weight towards destination state/cities
    count = len(states)
    print(states)
    for state in states: #TODO: Handle songs that are not available in spoyify
        songs = pd.read_csv(os.path.join(os.path.dirname(__file__), "../final_datasets/" + state + ".csv"))  # TODO: read from github instead of local
        songs = songs[songs["uris"] != "error"]
        songs = songs[songs["popularity"] != "0"]
        print("**********" + state)
        add_songs(playlist_id, songs, duration / count, sp, username)