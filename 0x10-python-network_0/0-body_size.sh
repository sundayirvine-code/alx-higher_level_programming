#!/bin/bash

# Take in the URL as the first command-line argument
url=$1

# Send a request to the URL and store the response body in a variable
response=$(curl -sS $url)

# Get the size of the response body in bytes and display it
size=$(echo $response | wc -c)
echo "${size}"

