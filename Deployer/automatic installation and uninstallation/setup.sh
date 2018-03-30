#!/bin/bash



#setup for each vm


#setting up for first vm (master vm)
sudo apt -y install python-pip
pip install requests
sudo apt update
sudo apt -y install docker.io
sudo docker pull cassandra 

input_ip=$(cat ip.txt)
total_ip=0
ip="ip"

IFS=' ' read -ra ADDR <<< "$input_ip"
for i in "${ADDR[@]}"; 
    do
    	((total_ip++))
    # process "$i"
    done

if [ "${total_ip}" -le 0 ]; then
    echo "installation done"
    exit 1


for i in $input_ip;
	do
		ssh -i ~/.ssh/smartdeployer ubuntu@$i "sudo apt -y install python-pip"
		ssh -i ~/.ssh/smartdeployer ubuntu@$i "pip install requests"
		ssh -i ~/.ssh/smartdeployer ubuntu@$i "sudo apt update"
		ssh -i ~/.ssh/smartdeployer ubuntu@$i "sudo apt -y install docker.io"
		ssh -i ~/.ssh/smartdeployer ubuntu@$i "sudo docker pull cassandra"
	done

 
# for first vm, init a swarm (this vm is swarm manager)
sudo docker swarm init > swarm.txt
swarm=$(python3 swarm.py)

for i in $input_ip;
	do
		ssh -i ~/.ssh/smartdeployer ubuntu@$i "sudo $swarm"
		
	done 

#set up the network for this machine
docker network create --driver overlay --scope swarm cassandra-net
# get the right compose file (note: this file could be pre-made by other script)



echo "installation done"

# get the result: 
# $ docker swarm join \
#     --token xxxxxxxxxxxxxxxxxx \
#     swarm_manager_ip:2377

# for other vm to join this swarm, run above command
# on other vm, after execute, it will give "this node joined a swarm as a worker"

# in case that people forget the join token, use command "sudo docker swarm join-token worker" to find
# 

# one silly way to update docker api version: uninstall docker, and install again 
# this ommand need docker api > 1.30


# create three docker cassandra services. To view the services: sudo docker service ls
# docker stack deploy ... will create 3 cassandra container in different vm (based on the tasks), we can benchmark on one of them
# create single service: sudo docker create --name <name_of_service> <container_image> <command to pass, usually it's "ping <swarm_manager_name>"
# to see where the container locatedm use command: sudo docker service tasks <name_of_service>
# services' resource can be limited.
# wget https://raw.githubusercontent.com/portworx/px-docs/gh-pages/scheduler/docker/portworx-cassandra3node.yaml
# docker stack deploy --compose-file portworx-cassandra3node.yaml cassandra 
