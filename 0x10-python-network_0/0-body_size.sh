#!/bin/bash
# Get the content length of the HTTP response header for a given URL.
curl -s "$1" | wc -c
