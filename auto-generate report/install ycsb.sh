#!/bin/bash
# this program automatically run five different workloads provided from ycsb
# the output files are named respectively: workloada.txt, workloadb.txt, workloadc.txt
# workloadd.txt, workloade.txt
# at the end the python script will output a nice table with all information
# cql file will clean all the database for next iteration

# required file:
# ycsb_setup.cql
# output.py
# ycsb_cleanup.cql

# download ycsb
# in the container
apt-get update
apt-get install curl
# obtain the ycsb
curl -O --location https://github.com/brianfrankcooper/YCSB/releases/download/0.12.0/ycsb-0.12.0.tar.gz
tar xfvz ycsb-0.12.0.tar.gz
rm ycsb-0.12.0.tar.gz


echo "ycsb installation finished"
exit 1




