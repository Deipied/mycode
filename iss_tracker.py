#!/usr/bin/env python3
"""Returning the location of the ISS in latitude/longitude"""
import requests
import datetime
import reverse_geocoder as rg

URL= "http://api.open-notify.org/iss-now.json"
def main():
    resp= requests.get(URL).json()
    lat = resp['iss_position']['latitude']
    lon = resp['iss_position']['longitude']
    coords_tuple = (lat, lon)
    result = rg.search(coords_tuple)
    time = datetime.datetime.fromtimestamp(resp['timestamp'])
    city= result[0]["name"]
    country= result[0]["cc"]
    print(f"CURRENT LOCATION OF THE ISS:\nTimestamp: {time}\nLon: {resp['iss_position']['longitude']}\nLat: {resp['iss_position']['latitude']}\nCity/Country: {city}, {country}")

if __name__ == "__main__":
    main()
