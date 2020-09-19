# Spotify Road Trip Playlist Generator

## Goal
Help users get a better sense of the history and culture of the cities that they are driving through, through personalized spotify playlists that comprise of songs that highlight the best of these cities


Idea Origin - On road trips, besides listening to just music that you like; it's nice to hear every once in a while a song about a place that you're driving through


## Components

* Create a database of songs associated with their corresponding geo locations 
   - https://en.wikipedia.org/wiki/List_of_songs_about_cities#United_States
      * has a good list of songs, but is heavily biased against smaller cities (eg. South Dakota has no representation :( )
   - https://www.lyrics.com
      * manually search by passing names of the big cities in each of the states
      * more comprehensive, but a lot of false positives
   - Besides just names of cities; it would be cool to have songs that are somehow related to a given city - for e.g. driving through S.D. you'd want to hear something about the Blackhills or Mount Rushmore - chances are that songs with words like these would have the name of one of the big cities in SD too, but it need not be the case. To capitalise on this maybe somehow use word vectors/https://relatedwords.org/relatedto/; This again leads to a lot of false positives

* Use google maps to find route (It would be really nice to have an add-on that shows you songs about places within a certain radius of you!)

* Create a personalised playlist based on user preferences (A favorite playlist? or top 100?) + route selected

* Build a nice UI
## TODO
* [ ] need to improve quality of queries
    * ~15% of songs scraped weren't able to be queried from spotify
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

## Prerequisites

- `pip3 install spotipy Flask Flask-Session`
* Python client for Google maps API: 

        $ pip install -U googlemaps

* Using the `dotenv` module to hide API keys:

        $ pip install python-dotenv
- Set the environment variables from your [app settings](https://developer.spotify.com/dashboard/applications). On Windows, use `set` instead of `export`.
    - `export SPOTIPY_CLIENT_ID=client_id_here`
    - `export SPOTIPY_CLIENT_SECRET=client_secret_here`

    - `export SPOTIPY_REDIRECT_URI=http://127.0.0.1:8080` 
        - must contain a port
        - `SPOTIPY_REDIRECT_URI` must be added to your [app settings](https://developer.spotify.com/dashboard/applications)
        
    - `export MAPS_API_KEY=your_google_api_key `

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

#### References
https://spotipy.readthedocs.io/en/2.13.0/

