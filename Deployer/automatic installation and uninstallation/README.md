# Description:
<strong/> setup.sh <strong/> will automatically install docker, and enable swarm mode for all the provided vm(instance) <br/>
uninstall.sh will automatically uninstall everything that is related to docker from all provided vm(instance)<br/>
note: all vm(instance) has to be existed at same subnet<br/>

# Instruction:
Installation:
1. create a file name "ip.txt" <br/>
2. put the vm's ip address (has to be private ip, and don't include the master vm's ip) into ip.txt, each ip is separated by space <br/>
3. run setup.sh  ``` $ ./setup.sh ```

Uninstallation:
1. make sure you still keep that ip.txt file
2. run uninstall.sh ```$ ./uninstall.sh ```


Note: cluster deploy file will be added later<br/>
Note: if you see "sudo unable to resolve host" in any of your vm, please see [Deployer](https://github.com/Zhipeng-Chang/CMPUT-401-Winter-2018/tree/master/Deployer) README.md
