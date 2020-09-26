import random
import pandas as pd
import os

from utils.route import states_along_route
from utils.route import trip_duration_seconds

class Playlist:
    def __init__(self, origin, destination, playlist_name, spotify, username):
        self.origin = origin
        self.destination = destination
        self.playlist_name = playlist_name
        self.spotify = spotify
        self.username = username
        self.playlist_id = self.search_playlist_id()
        self.states = list(states_along_route(self.origin, self.destination).keys())
        self.duration = trip_duration_seconds(self.origin, self.destination) * 1000*0.9

    # Done
    def search_playlist_id(self):
        playlist_id = ""
        playlists = self.spotify.user_playlists(self.username)
        for playlist in playlists["items"]:
            if (playlist["name"] == self.playlist_name):
                playlist_id = playlist["id"]
        return playlist_id
    #
    def create_playlist(self):
        # See if playlist already exists
        # if exists, return playlist id
        # else create new one
        # TODO: Complete this function
        if (self.playlist_id == ""):
            self.spotify.user_playlist_create(self.username, self.playlist_name, public=True)
            self.search_playlist(self.spotify, self.username, self.playlist_name)
            return (self.playlist_id, True)
        return (self.playlist_id, False)

    #def similarity_matrix():
        # creaate similarity matrix
        # find the most similar/ppoular songs from users existing playlist
        # return song

    def make_roadtrip_playlist(self):
        count = len(self.states)
        print(self.states)
        for state in self.states: #TODO: Handle songs that are not available in spoyify
            songs = pd.read_csv(os.path.join(os.path.dirname(__file__), "../create_data/merged_final/" + state + ".csv"))  # TODO: read from github instead of local
            print("**********" + state)
            self.add_songs( songs, self.duration / count)

    def add_songs(self, songs, duration):
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

            if bag.loc[bag.index[0], 'song'] not in song_set:
                song_set.add(bag.loc[bag.index[0], 'song'])
                uri = bag.loc[bag.index[0], 'uris']  # TODO: change to column name later
                song_length = int(bag.loc[bag.index[0], 'duration_ms'])
                self.spotify.user_playlist_add_tracks(self.username, playlist_id=self.playlist_id, tracks=[uri], position=None)
                duration = duration - song_length
            else:
                count+=1
