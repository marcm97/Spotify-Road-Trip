import os
from dotenv import load_dotenv
import googlemaps
from datetime import datetime
from collections import Counter

load_dotenv()
# Loading secret API key stored in .env file
API_KEY = os.getenv('MAPS_API_KEY')

gmaps = googlemaps.Client(key=API_KEY)

def states_along_route(origin, destination):
    # Request driving instructions
    now = datetime.now()
    directions_result = gmaps.directions(origin,
                                        destination,
                                        mode="driving",
                                        departure_time=now)
    threshold = 150000
    result = []
    legs = directions_result[0]['legs']
    
    for leg in legs:
        # Each leg of the route has 1 or more steps
        steps = leg['steps']
        # Extract the end_location lat and long from each step and find the location at those coordinates
        for step in steps:
#             geocode = (step['end_location']['lat'], step['end_location']['lng'])
#             print(geocode, step['distance'])
            if step['distance']['value'] > threshold:
                 break_up_step(step, threshold)
            address = gmaps.reverse_geocode(step['end_location'], result_type='administrative_area_level_1')
            result.append(address[0]['address_components'][0]['long_name'])

    count_states = Counter(result)  
    return dict(count_states) #TODO: select songs based on the time spent in each state

def break_up_step(step, threshold):
    pieces = step['distance'] #TODO: split a long trip into two

def trip_duration_seconds(origin, destination):
    now = datetime.now()
    directions_result = gmaps.directions(origin,
                                        destination,
                                        mode="driving",
                                        departure_time=now)
    return directions_result[0]['legs'][0]['duration']['value']