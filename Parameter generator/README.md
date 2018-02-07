Description:

Will generate a set of input parameters for the deployer to configure the containers and Cassandra on the given set of VMs. The program might also be to take output from the visualizer to optimize the parameter settings. The core of the smart aspect will be based on the Monte Carlo method and the program will explore the parameter space based on the values calculated until ultimately reaching an optimized parameter setting for the deployment target.


Programming language:
Python

# Initial stage:

Parameters may have impact on Docker: memory, CPU and block I/O.
(Reference: https://docs.docker.com/config/containers/resource_constraints/)

Parameters may have impact on Cassandra: commit log, compaction, memory, disk I/O, CPU, reads, and writes.
(Reference: https://docs.datastax.com/en/cassandra/3.0/cassandra/configuration/configCassandra_yaml.html#configCassandra_yaml__PerformanceTuningProps)

# 2018/02/06 Update:

This is just a blueprint for the analyzing part, need to be discussed. 

Updated a code for analyzing the output from YCSB. This code is assuming the output has several input parameters and only one single output (specifically, the respons time of YCSB). The way of analyzing is: separate all outputs into several groups (in the example below, 10 groups), and for each group, find how many times each setting been used, shows as percentage. 

Example:

https://github.com/Zhipeng-Chang/CMPUT-401-Winter-2018/blob/master/Parameter%20generator/Example%20output.png

For the example in this folder, I made 250 sets of data. For each group of data, there are 5 numbers, first four numbers are the inputs for YCSB, let's say there are the CPU, disk, memory and I/O, the last number is the respons time (output). For each input parameters, using a number to represent it, for example, if I have memory for 1GB, 2GB, 3GB, 4GB, it will be represented by 1 2 3 4. If there is only enable or disable for I/O, then using 1 or 0 to represent.  

The final result could show for each group, what kind of setting has been used a lot. We could use the setting from the faster group namely from the group 101-200. And avoid the setting from the slow respons group, groups like 701-800, 801-900, 901-1000.







