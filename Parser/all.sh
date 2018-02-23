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


# set_up the ycsb
cqlsh -e "create keyspace if not exists ycsb WITH REPLICATION = {'class' : 'SimpleStrategy', 'replication_factor': 1 };"
cqlsh -e "create table ycsb.usertable (y_id varchar primary key, field0 varchar, field1 varchar, field2 varchar, field3 varchar, field4 varchar, field5 varchar, field6 varchar, field7 varchar, field8 varchar, field9 varchar) with compression = {'sstable_compression': ''};"


# step 1. get the ip address
# make the output as variable
# OUTPUT="$(ls -1)"
# echo "${OUTPUT}"
nodetool status ycsb > hostIP.txt
IP_address = "$(python getHostIp.py)"


# step 2. generate five report
declare -a arr=("a" "b" "c" "d" "e")
for i in "${arr[@]}"
do
./ycsb-0.12.0/bin/ycsb load cassandra-cql -p hosts=${IP_address} -P ./ycsb-0.12.0/workloads/workload${i} -s > ../workload_load_output${i}.txt
./ycsb-0.12.0/bin/ycsb run  cassandra-cql -p hosts=${IP_address} -P ./ycsb-0.12.0/workloads/workload${i} -s > ../workload_run_output${i}.txt
# or do whatever with individual element of the array
done


# give the general report via python file
python generate_report.py

# clean up the ycsb
cqlsh -e "drop table ycsb.usertable;"

echo "finished"
exit 1




