#!/bin/bash
# Script to automatically deploy the execution environment

# Initial Version 1.0

# fix sudo command: https://askubuntu.com/questions/59458/error-message-sudo-unable-to-resolve-host-user
#   fixed:That the /etc/hostname file contains just the name of the machine.
#
#   That /etc/hosts has an entry for localhost. It should have something like:
#
#       127.0.0.1    localhost.localdomain localhost
#       127.0.1.1    my-machine
#   note: if the hosts file can't be modified due to permission deny; use:  $sudo nano hosts


curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt-get update

# install docker
sudo apt-get install -y docker-ce


# all setup, docker is running, pull cassandra from docker hub
sudo docker pull cassandra

# run cassandra
sudo docker run -d -P --name demo cassandra


# running a docker container
sudo docker container start demo

# get into the container
sudo docker exec -it demo bash





