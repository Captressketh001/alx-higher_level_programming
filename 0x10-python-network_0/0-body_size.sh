#!/bin/bash
# Bash script that takes in a URL
# sends a request to that URL
# displays the size of the body of the response

response=$(mktemp)
curl -s -o $response $1

size=$(wc -c < $response)
echo $size

# remove the temporary file
rm $response
