## compute_input.py

import json
import sys
from datetime import datetime

import googlemaps

# Read data from stdin
from Trans_Mode import Walk, Drive


def read_in():
    lines = sys.stdin.readlines()
    # Since our input would only be having one line, parse our JSON data from that
    return json.loads(lines[0])


def main():
    gmaps = googlemaps.Client(key='AIzaSyB-Tl6HY9naSBAfJc0KjAg-0yXIlxrTqOA')

    now = datetime.now()
    directions_result = gmaps.directions(sys.argv[1], sys.argv[2],
                                         mode="transit",
                                         departure_time=now,
                                         language='en-GB')
    result = ""
    # for step in directions_result[0]['legs'][0]['steps']:
    #
    #     if step['travel_mode'] == 'WALKING':
    #         result += Walk(step)


    directions_result = gmaps.directions(sys.argv[1], sys.argv[2],
                                         mode="driving",
                                         departure_time=now,
                                         language='en-GB')
    # print(directions_result[0]['legs'][0])
    result += str(Drive(directions_result[0]['legs'][0]))

    # if 'transit_details' in step:
    #     for detail in step['transit_details']:
    #         print(detail)
    print(result,end = "")

# start process
if __name__ == '__main__':
    main()
