#!/bin/bash
# This script sends a DELETE request to the URL passed as the first argument and displays the body of the response.

# Check if a URL is provided
if [ -z "$1" ]; then
  echo "Please provide a URL"
  exit 1
fi

# Send DELETE request and display the body of the response
curl -sX DELETE "$1"

