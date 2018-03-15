#!/bin/bash



#setup for each vm


#uninstallfor first vm (master vm)
sudo systemctl stop docker
sudo apt-get purge -y docker-engine docker docker.io docker-ce
sudo apt-get autoremove -y --purge docker-engine docker docker.io docker-ce
sudo apt-get autoclean

sudo rm -rf /var/lib/docker
sudo rm /etc/apparmor.d/docker
sudo groupdel docker

input_ip=$(cat ip.txt)
total_ip=0
ip="ip"

IFS=' ' read -ra ADDR <<< "$input_ip"
for i in "${ADDR[@]}"; 
    do
    	((total_ip++))
    # process "$i"
    done

for i in $input_ip;
	do
		ssh -i ~/.ssh/smartdeployer ubuntu@$i "sudo systemctl stop docker "
		ssh -i ~/.ssh/smartdeployer ubuntu@$i "sudo apt-get purge -y docker-engine docker docker.io docker-ce"
		ssh -i ~/.ssh/smartdeployer ubuntu@$i "sudo apt-get autoremove -y --purge docker-engine docker docker.io docker-ce"
		ssh -i ~/.ssh/smartdeployer ubuntu@$i "sudo apt-get autoclean"
		ssh -i ~/.ssh/smartdeployer ubuntu@$i "sudo rm -rf /var/lib/docker"
		ssh -i ~/.ssh/smartdeployer ubuntu@$i "sudo rm /etc/apparmor.d/docker"
		ssh -i ~/.ssh/smartdeployer ubuntu@$i "sudo groupdel docker"
	done


echo "unistallation done"

