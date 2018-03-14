#!/bin/bash

# smartdeployer test script
# test on if files installed successfully in right place

total_tests=0
passed_tests=0
# first check if docker installed
docker -v
output=$(echo $?)

((total_tests+=1))
if [ "$output" -eq 0 ]; then
    echo "Docker installed" >&2
    ((passed_tests+=1))
else
    echo "Docker NOT installed" >&2
fi


# check if Cassandra installed
service cassandra status
output=$(echo $?)

((total_tests+=1))
if [ "$output" -eq 0 ]; then
echo "Cassandra installed" >&2
((passed_tests+=1))
else
echo "Cassandra NOT installed" >&2

fi

# More tests will be updated in terms of the progress of the project

echo "Passed $passed_tests in $total_tests Total tests"

exit 0
















