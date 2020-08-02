# Goal: Help users get a better sense of the history and culture of the cities that they are driving through, through personalized spotify playlists that comprise of songs that highlight the best of these cities

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
