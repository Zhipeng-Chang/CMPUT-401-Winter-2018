#!/bin/bash

# smartdeployer install script
# version 1.0

#default setting
CONTAINTERS=1
OPTIMIZE="OFF"

#docker installation function

function install_docker {

    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
    sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
    sudo apt-get update

    # install docker
    sudo apt-get install -y docker-ce

    # all setup, docker is running, pull cassandra from docker hub
    sudo docker pull cassandra

}



POSITIONAL=()
while [[ $# -gt 0 ]]
do
key="$1"
 
case $key in
    -c|--container)
    CONTAINTERS="$2"
    shift # past argument
    shift # past value
    ;;
    -o|--optimize)
    OPTIMIZE="$2"
    shift # past argument
    shift # past value
    ;;
    # -l|--lib)
    # LIBPATH="$2"
    # shift # past argument
    # shift # past value
    # ;;
    # --default)
    # DEFAULT=YES
    # shift # past argument
    # ;;
    # *)    # unknown option
    # POSITIONAL+=("$1") # save it in an array for later
    # shift # past argument
    # ;;
esac
done

set -- "${POSITIONAL[@]}" # restore positional parameters
 
# echo Numbers of Containers  = "${CONTAINTERS}"
# echo Optimization is = "${OPTIMIZE}"

#if user input is less than 0: warning; if user input is greater than 100 (number may fix), warning
#  ${CONTAINERS} will return int, not string
if [ "${CONTAINTERS}" -le 0 ]; then
    echo Containers number has to greater than 0
    exit 1

elif [ "${CONTAINTERS}" -gt 100 ]; then
    echo Containers number is way too big
    exit 1
fi



# optimization option;
# space matters!!!  ["$OPTIMIZE" == "ON"] won't work
if [ "$OPTIMIZE" == "ON" ]; then

    echo "optimize ON"
    install_docker
    for ((container_num=0;container_num<${CONTAINTERS};container_num++))
        do
            sudo docker run -d -P --name "demo"$container_num cassandra
        done
    echo "${CONTAINTERS} containers generated."
    #show all the created containers
    sudo docker stats -a --no-stream
    

    
elif [ "$OPTIMIZE" == "OFF" ]; then
    echo "optimize OFF"
    install_docker
    for ((container_num=0;container_num<${CONTAINTERS};container_num++))
        do
            sudo docker run -d -P --name "demo"$container_num cassandra
        done
        
else
    echo "Please choose ON or OFF for optimize option (Capitalized)"
fi
























