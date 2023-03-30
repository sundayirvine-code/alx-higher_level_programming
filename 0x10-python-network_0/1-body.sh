#!/bin/bash
# This script takes a URL as an argument, sends a GET request to that URL, and displays the body of the response.

# Check if a URL is provided
if [ -z "$1" ]; then
  echo "Please provide a URL"
  exit 1
fi

# Send request and display the body of the response
curl -sL -w "%{http_code}" "$1" -o /dev/null | {
  read -r code
  if [ "$code" -eq 200 ]; then
    curl -s "$1"
  fi
}

