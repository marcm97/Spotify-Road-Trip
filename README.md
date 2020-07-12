# Create a list of songs about all places in America

## Components
* webscrape from various sources
* query from spotify api  
* song name; spotify uri

## TODO
* [ ] need to improve quality of queries
    * ~1000/10000 songs weren't able to be queried from spotify
    * try out the fuzzy wuzzy api?

## Open Questions
* instead of csv, with 10,000+ songs would a db be better?
* Figure out how to extract places from route:
    * Look at `html_instructions`? Maybe just use lat, longs along route to query Places API? Or maybe there's some 
    standard way to do this - need to keep looking.

## Notes
* Spotify authentication

* Map
http://amunategui.github.io/yelp-v3-cross-country-trip/index.html

* Flask APP

* Python client for Google maps API: 

        $ pip install -U googlemaps

* Using the `dotenv` module to hide API keys:

        $ pip install python-dotenv
