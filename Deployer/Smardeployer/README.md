# Smartdeployer Usage:
## Instruction:
Grant the permission to smartdeployer.sh
```chmod u+x smartdeployer.sh```

Installation:
1. create a file name "ip.txt" <br/>
2. put the vm's ip address (has to be private ip, and don't include the master vm's ip) into ip.txt, each ip is separated by space <br/>
3. run install ``` $ ./smartdeployer.sh <your_keypair_name> install ```

Uninstallation:
1. make sure you still keep that ip.txt file
2. run uninstall ```$ ./smartdeployer.sh <your_keypair_name> uninstall ```

Update:
1. make sure you still keep that ip.txt file
2. run update ```$ ./smartdeployer.sh <your_keypair_name> update ```



Note: cluster deploy file will be added later<br/>
Note: if you see "sudo unable to resolve host" in any of your vm, please see [Deployer](https://github.com/Zhipeng-Chang/CMPUT-401-Winter-2018/tree/master/Deployer) README.md
