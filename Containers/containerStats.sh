#!/bin/bash

# this script will get the container stats
# every 5 min and pipe it to a txt file for visualization

while true; do
echo 'more stats' 
docker stats --format "{{.Container}}:{{.NetIO}}" > stats.text
sleep 300 
done 