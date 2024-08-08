#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status using requests"""
import requests

if __name__ == "__main__":
    """Fetches https://intranet.hbtn.io/status using requests"""
    try:
        # Send GET request
        r = requests.get('https://intranet.hbtn.io/status')
        
        # Ensure we handle redirection correctly (if applicable)
        r.raise_for_status()  # Raise an exception for HTTP errors
        
        # Print response details
        print("Body response:")
        print("\t- type: {}".format(type(r.text)))
        print("\t- content: {}".format(r.text.strip()))
        
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

