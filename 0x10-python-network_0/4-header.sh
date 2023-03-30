#!/bin/bash
# This script takes a URL as an argument, sends a GET request to the URL with a custom header, and displays the response body.

# Check if a URL is provided
if [ -z "$1" ]; then
  echo "Please provide a URL"
  exit 1
fi

# Send a GET request with a custom header and display the response body
curl -sH "X-School-User-Id: 98" "$1"

