#!/usr/bin/env python3
"""Returning the location of the ISS in latitude/longitude"""
import requests



NASA= "http://api.open-notify.org/iss-now.json"
def main():
    resp= requests.get(NASA).json()
    
    print("Current location of the ISS: ")
    print("Lon: ", resp["iss_position"]["longitude"])
    print("Lat: ", resp["iss_position"]["latitude"])
    
    
if __name__ == "__main__":
    main()
