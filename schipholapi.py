#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import sys
import optparse

def callPublicFlightAPI():
    url = 'https://api.schiphol.nl/public-flights/flights'

    headers = {
	  'resourceversion': 'v4',
      'app_id': 'a4cd254b',
	  'app_key': '9c9bcb494d0096895d4aaecc9f96a984',
      'Accept': 'application/json'
	}

    response = requests.request('GET', url, headers=headers)

    if response.status_code == 200:
        flightList = response.json()
        print('found {} flights.'.format(len(flightList['flights'])))
        for flight in flightList['flights']:
            print('Found flight with name: {} scheduled on: {} at {}'.format(flight['flightName'
                    ], flight['scheduleDate'], flight['scheduleTime']))
    else:
        print('''Oops something went wrong
Http response code: {}
{}'''.format(response.status_code,
                response.text))

    return flightList

flightList = callPublicFlightAPI()