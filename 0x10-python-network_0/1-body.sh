#!/bin/bash
# Bash script that takes in a URL
# sends a GET request to the URL
# displays the body of the response

curl -sL "$1"
