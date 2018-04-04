#!/bin/bash



#setup for each vm
POSITIONAL=()
while [[ $# -gt 0 ]]
do
key="$1"
 
case $key in
    -k|--keyname)
    KEYNAME="$2"
    shift # past argument
    shift # past value
esac
done

set -- "${POSITIONAL[@]}" # restore positional parameters


# warning user ;)
while true; do
    read -p "If you don't follow instruction, the script will mess up your computer. Understood?" yn
    case $yn in
        [Yy]* ) break;;
        [Nn]* ) exit;;
        * ) echo "Please answer yes or no.";;
    esac
done



#setting up for first vm (master vm)
sudo apt-get update
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo apt-add-repository 'deb https://apt.dockerproject.org/repo ubuntu-trusty main'

sudo apt-get install apt-transport-https ca-certificates curl software-properties-common
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu xenial stable"

sudo apt-get update
echo "y" | sudo apt-get install docker-ce
sudo docker pull cassandra
sudo docker pull webscam/cassandra:3.10

sudo docker swarm init > swarm.txt


# test if ip.txt exist
input_ip=$(cat ip.txt)
if [ "$input_ip" == "cat: ip.txt: No such file or directory" ]
then
      echo "can't find ip.txt (program exit)"
      exit 1
fi


# test if ip.txt is empty
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
fi

# test if the key is empty
if [ -z "$KEYNAME" ];
	then
	echo "Please input your key name (more detail see readme)"
	exit 1
fi


for i in $input_ip;
	do
		ssh -i ~/.ssh/$KEYNAME ubuntu@$i "sudo apt-get update"
		ssh -i ~/.ssh/$KEYNAME ubuntu@$i "sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -"
		ssh -i ~/.ssh/$KEYNAME ubuntu@$i "sudo apt-add-repository 'deb https://apt.dockerproject.org/repo ubuntu-trusty main'"
		ssh -i ~/.ssh/$KEYNAME ubuntu@$i "sudo add-apt-repository 'deb [arch=amd64] https://download.docker.com/linux/ubuntu xenial stable'"
		ssh -i ~/.ssh/$KEYNAME ubuntu@$i "sudo apt-get update"
		ssh -i ~/.ssh/$KEYNAME ubuntu@$i "echo 'y' | sudo apt-get install docker-ce"
		ssh -i ~/.ssh/$KEYNAME ubuntu@$i "sudo docker pull cassandra"
		ssh -i ~/.ssh/$KEYNAME ubuntu@$i "sudo docker pull webscam/cassandra:3.10"
	done

 
# for first vm, init a swarm (this vm is swarm manager)

swarm=$(python3 swarm.py)

for i in $input_ip;
	do
		ssh -i ~/.ssh/$KEYNAME ubuntu@$i "sudo $swarm"
		
	done 

#set up the network for this machine
sudo docker network create --driver overlay --scope swarm cassandra-net
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
