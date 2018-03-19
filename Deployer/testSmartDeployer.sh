#!/bin/bash

# smartdeployer test script
# test on if files installed successfully in right place
# also, the sript will test the workingenvironment of the software

echo ""
echo "Starting Bash test . . ."
echo ""


total_tests=0
passed_tests=0

# check network #source:https://stackoverflow.com/questions/17291233/how-to-check-internet-access-using-bash-script-in-linux
((total_tests+=1))
wget -q --tries=10 --timeout=20 --spider http://google.com &> /dev/null # hide output
if [[ $? -eq 0 ]]; then
((passed_tests+=1))
echo "Online"
else
echo "Offline"
fi

# check JAVA
((total_tests+=1))
output=$(java -version) &> /dev/null
if [[ "$output" -eq 0 ]]; then
((passed_tests+=1))
echo "JAVA version corrent"
else
echo "Incorrect JAVA version "
fi


# check JAVA
((total_tests+=1))
output=$(python --version) &> /dev/null
if [[ "$output" -eq 0 ]]; then
((passed_tests+=1))
echo "python version corrent"
else
echo "Incorrect python version "
fi


# first check if docker installed
docker -v &> /dev/null
output=$(echo $?) &> /dev/null

((total_tests+=1))
if [ "$output" -eq 0 ]; then
    echo "Docker installed" >&2
    ((passed_tests+=1))
else
    echo "Docker NOT installed" >&2
fi


# check if Cassandra installed
service cassandra status &> /dev/null
output=$(echo $?) &> /dev/null

((total_tests+=1))
if [ "$output" -eq 0 ]; then
echo "Cassandra installed" >&2
((passed_tests+=1))
else
echo "Cassandra NOT installed" >&2

fi

# More tests will be updated in terms of the progress of the project

echo ""
echo "Passed $passed_tests in $total_tests Total tests"
echo ""
exit 0
















