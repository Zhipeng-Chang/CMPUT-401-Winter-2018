Description:

Will generate a set of input parameters for the deployer to configure the containers and Cassandra on the given set of VMs. The program might also be to take output from the visualizer to optimize the parameter settings. The core of the smart aspect will be based on the Monte Carlo method and the program will explore the parameter space based on the values calculated until ultimately reaching an optimized parameter setting for the deployment target.


Programming language:
Python

## Initial stage:

# Parameters may have impact on Docker: memory, CPU and block I/O.

(Reference: https://docs.docker.com/config/containers/resource_constraints/)

# Parameters may have impact on Cassandra: commit log, compaction, memory, disk I/O, CPU, reads, and writes.
(Reference: https://docs.datastax.com/en/cassandra/3.0/cassandra/configuration/configCassandra_yaml.html#configCassandra_yaml__PerformanceTuningProps)



## Next stage:

# Need to test and make decision what paramrters will be changed to optimiza the overall performance.







