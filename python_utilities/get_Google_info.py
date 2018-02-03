## compute_input.py

import json
import sys
import googlemaps
from datetime import datetime


# Read data from stdin
from Trans_Mode import Walk


def read_in():
    lines = sys.stdin.readlines()
    # Since our input would only be having one line, parse our JSON data from that
    return json.loads(lines[0])


def main():
    # get our data as an array from read_in()
    # lines = read_in()

    # print(lines)

    # create a numpy array

    # return the sum to the output stream


    gmaps = googlemaps.Client(key='AIzaSyB-Tl6HY9naSBAfJc0KjAg-0yXIlxrTqOA')

    # Geocoding an address
    geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

    # Look up an address with reverse geocoding
    reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))


    # Request directions via public transit
    now = datetime.now()
    directions_result = gmaps.directions("Sydney Town Hall",
                                         "Parramatta, NSW",
                                         mode="transit",
                                         departure_time=now)

    for step in directions_result[0]['legs'][0]['steps']:

        # print(step['travel_mode'])
        if step['travel_mode'] == 'WALKING':
            print(Walk(step))


        # if 'transit_details' in step:
        #     for detail in step['transit_details']:
        #         print(detail)


# start process
if __name__ == '__main__':
    main()
