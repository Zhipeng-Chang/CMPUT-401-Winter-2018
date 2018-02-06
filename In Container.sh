#!/bin/bash
# Script to automatically deploy the execution environment

# Initial Version 1.0

# in the container
sudo apt-get update

#configure the cassandra


apt-get install curl
# obtain the ycsb
curl -O --location https://github.com/brianfrankcooper/YCSB/releases/download/0.12.0/ycsb-0.12.0.tar.gz
tar xfvz ycsb-0.12.0.tar.gz
rm ycsb-0.12.0.tar.gz
cd ycsb-0.12.0
#         # run ycsb
#         ./bin/ycsb

         # create a cassandra table: run cassandra query language
#         cqlsh
#         # create keyspace, table, data with cassandra
#         > create keyspace testKeyspace with replication = {'class':'SimpleStrategy','replication_factor': 3} ;
#         >create table test (testUsr text, testpass text, primary key(testUsr));
#         >insert into test (testUsr,testpass) values ('xcao','2333');
#         # to use ycsb to against cassandra to test performance, create the ycsb keyspaces;
#         https://github.com/brianfrankcooper/YCSB/tree/master/cassandra
#         //cqlsh> create keyspace ycsb
#         WITH REPLICATION = {'class' : 'SimpleStrategy', 'replication_factor': 3 };
#         cqlsh> USE ycsb;
#         cqlsh> create table usertable (
#         y_id varchar primary key,
#         field0 varchar,
#         field1 varchar,
#         field2 varchar,
#         field3 varchar,
#         field4 varchar,
#         field5 varchar,
#         field6 varchar,
#         field7 varchar,
#         field8 varchar,
#         field9 varchar);



#  cassandra configuration file is in cassandra.yaml
#  cd /etc/cassandra/cassandra.yaml
# http://docs.datastax.com/en/cassandra/2.1/cassandra/configuration/configCassandra_yaml_r.html#configCassandra_yaml_r__PerformanceTuningProps
# this contain the main factors that could optimize the performance of cassandra

# run ycsb against cassandra 
# cassandra-cql or cassandra2-cql
# workloads could be workloada to workloadn
./bin/ycsb load cassandra-cql -s -P workloads/workloada > output.txt

# save the progress

echo "Installation complete."
exit 1





