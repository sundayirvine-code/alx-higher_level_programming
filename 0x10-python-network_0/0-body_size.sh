#!/bin/bash
# This script takes a URL as an argument, sends a request to that URL, and displays the size of the body of the response in bytes.

# Check if a URL is provided
if [ -z "$1" ]; then
  echo "Please provide a URL"
  exit 1
fi

# Send request and display the size of the body
curl -sI "$1" | grep -i "Content-Length" | awk '{print $2}'

