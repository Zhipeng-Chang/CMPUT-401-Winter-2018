#!/bin/bash



echo "script is running..."


POSITIONAL=()
while [[ $# -gt 0 ]]
do
key="$1"

 
case $key in
    -m|--memory)
    MEMORY="$2"
    shift # past argument
    shift # past value
    ;;
    -c|--cpu)
    CPU="$2"
    shift # past argument
    shift # past value
    ;;
    -b|--blkio)
    BLKIO="$2"
    shift # past argument
    shift # past value
    ;;
esac
done

set -- "${POSITIONAL[@]}" # restore positional parameters

sudo docker update --cpus=$CPU -m=$MEMORY"m" --blkio-weight=$BLKIO "test_container"
sudo docker exec -it "test_container" ./allv2.sh -c $CPU -m $MEMORY"m" -b $BLKIO


echo "script is done..."
exit 1












































