#!/bin/bash
# This script takes a URL as an argument, sends a POST request to the URL with two parameters, and displays the response body.

# Check if a URL is provided
if [ -z "$1" ]; then
  echo "Please provide a URL"
  exit 1
fi

# Send a POST request with two parameters and display the response body
curl -s -X POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"

