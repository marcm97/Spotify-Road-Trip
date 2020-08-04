# Spotify Road Trip Playlist Generator

## Goal
Help users get a better sense of the history and culture of the cities that they are driving through, through personalized spotify playlists that comprise of songs that highlight the best of these cities

## Components
* webscrape from various sources
* query from spotify api  
* use google maps to find route
* build UI

## TODO
* [ ] need to improve quality of queries
    * ~10% of songs scraped weren't able to be queried from spotify
    * try out the fuzzy wuzzy api?
    * besides songs that just contain the names of cities that you pass through, also find songs about things associated with a city
    https://relatedwords.org/relatedto/ or word2vec?

## Open Questions
* instead of csv, with 100,000+ songs would a db be better?
* Figure out how to extract places from route:
    * Using `reverse_geocode` is extremely slow - need to find a better way
* How can we geotag songs at a granular level (exact location)
* can we get songs ordered in such a way that we hear them as we pass through?

## Notes
* Spotify authentication, Spotipy

* Map
http://amunategui.github.io/yelp-v3-cross-country-trip/index.html

* Flask APP

* Python client for Google maps API: 

        $ pip install -U googlemaps

* Using the `dotenv` module to hide API keys:

        $ pip install python-dotenv

## Prerequisites

- `pip3 install spotipy Flask Flask-Session`
- Set the environment variables from your [app settings](https://developer.spotify.com/dashboard/applications). On Windows, use `set` instead of `export`.
    - `export SPOTIPY_CLIENT_ID=client_id_here`
    - `export SPOTIPY_CLIENT_SECRET=client_secret_here`

    - `export SPOTIPY_REDIRECT_URI=http://127.0.0.1:8080` 
        - must contain a port
        - `SPOTIPY_REDIRECT_URI` must be added to your [app settings](https://developer.spotify.com/dashboard/applications)

- Add your Google API key in the [templates\home.html](https://github.com/marcm97/Spotify-Road-Trip/blob/599a3d2d291890108833487c551a8dfbb11c830a/templates/home.html#L7) file
- Run app.py
    - `python3 -m flask run --port=8080`
        - If receiving `port already in use` error, try other ports: 5000, 8090, 8888, etc...
(will need to be updated in your Spotify app and SPOTIPY_REDIRECT_URI variable)

#### Optional

In development environment for debug output
- `export FLASK_ENV=development`

So that you can invoke the app outside of the file's directory include
- `export FLASK_APP=/path/to/spotipy/examples/app.py`


