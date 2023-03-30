#!/bin/bash
# This script takes a URL as an argument and displays all HTTP methods the server will accept.

# Check if a URL is provided
if [ -z "$1" ]; then
  echo "Please provide a URL"
  exit 1
fi

# Send an OPTIONS request and display the Allow header
curl -sI "$1" | grep "Allow" | cut -d " " -f2-

