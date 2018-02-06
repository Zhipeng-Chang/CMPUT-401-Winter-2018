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

#ask user whether choose defualt preformance or optimazed preformance
echo "Do you wish to build the container with optimzed set?[Y/N]"
read user_choice_of_setting_of_container



#ask user how many container they need
echo Enter number of containers:
read num_of_container

# run cassandra
sudo docker run -d -P --name demo cassandra
# you can set the performance when you start to run the images that pulled; below is the example from:
# https://docs.docker.com/config/containers/resource_constraints/
# https://bobcares.com/blog/docker-performance/2/
# the most important parameter: CPU; memory; I/O;   do we need the reference to support our claims?
# create the data based on the stuff automatically
# docker run --it --cpu-rt-runtime=950000 \
#                   --ulimit rtprio=99 \
#                   --cap-add=sys_nice \
#                   debian:jessie

# # automatically strategy: 
# for container_number in range(userinput):
# 	sudo docker run -d -P --name demo+container_number cassandra
# 	# the container name will be demo1 demo2 demo3 ...
# 	sudo docker exec -it demo+container_number bash
# 	# get into the container, auto configure the cassandra (cassandra.yaml file) exit for creating next container



# question: if you want to optimize the cassandra on all the container that you created,
# do you need to go one by one to configure
# or you can just configure at one container, and other container will autoamtically follow the same configuration?
done



# running a docker container
sudo docker container start demo

# get into the container
sudo docker exec -it demo bash





