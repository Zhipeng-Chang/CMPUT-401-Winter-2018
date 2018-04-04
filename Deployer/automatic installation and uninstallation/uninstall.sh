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


#uninstallfor first vm (master vm)
sudo systemctl stop docker
sudo apt-get purge -y docker-engine docker docker.io docker-ce
sudo apt-get autoremove -y --purge docker-engine docker docker.io docker-ce
sudo apt-get autoclean

sudo rm -rf /var/lib/docker
sudo rm /etc/apparmor.d/docker
sudo groupdel docker

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
		ssh -i ~/.ssh/$KEYNAME ubuntu@$i "sudo systemctl stop docker "
		ssh -i ~/.ssh/$KEYNAME ubuntu@$i "sudo apt-get purge -y docker-engine docker docker.io docker-ce"
		ssh -i ~/.ssh/$KEYNAME ubuntu@$i "sudo apt-get autoremove -y --purge docker-engine docker docker.io docker-ce"
		ssh -i ~/.ssh/$KEYNAME ubuntu@$i "sudo apt-get autoclean"
		ssh -i ~/.ssh/$KEYNAME ubuntu@$i "sudo rm -rf /var/lib/docker"
		ssh -i ~/.ssh/$KEYNAME ubuntu@$i "sudo rm /etc/apparmor.d/docker"
		ssh -i ~/.ssh/$KEYNAME ubuntu@$i "sudo groupdel docker"
	done


echo "unistallation done"

