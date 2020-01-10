#! /usr/bin/env python3


# sample json received from purpleair.com
#
# {'version': '7.0.4', 'fields': ['ID', 'pm', 'age', 'pm_0', 'pm_1', 'pm_2', 'pm_3', 'pm_4', 'pm_5', 'pm_6', 'conf', 'pm1', 'pm_10', 'p1', 'p2', 'p3', 'p4', 'p5', 'p\
6', 'Humidity', 'Temperature', 'Pressure', 'Elevation', 'Type', 'Label', 'Lat', 'Lon', 'Icon', 'isOwner', 'Flags', 'Voc', 'Ozone1', 'Adc', 'CH'], 'data': [[37123, 10\
.1, 1, 10.1, 8.8, 6.1, 4.9, 4.1, 7.1, 10.6, 100, 6.9, 10.7, 1430.7, 406.0, 56.9, 4.1, 1.0, 0.6, 61, 53, 1021.75, 9, 0, 'Actual Name on Record', 37.850136, -122.29151\
, 0, 0, 0, None, None, 0.0, 3]], 'count': 1}


import requests
import json
import sys
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("URL")
parser.add_argument("-v", action='store_true', help='print debugging information')
args = parser.parse_args()


r = requests.get(args.URL)


if r.status_code != requests.codes.ok:
    # todo: 429 is too many requests, perhaps a time.sleep in a loop to re-request
    if args.v:
        print('bad status:', r.status_code)
    sys.exit(1)

if args.v:
    print('status:', r.status_code)
    print('text:', r.text)
    print('json:', r.json())


try:
    j = r.json()
except json.decoder.JSONDecodeError:
    if args.v:
        print('exception:')
        print(r.raw.read())
        print()
    sys.exit(2)
