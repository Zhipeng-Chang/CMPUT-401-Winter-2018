#Output the graph of the YSCB result
#version 0.1 demo use
#Modified from report generator in the same project
#Source:https://github.com/Zhipeng-Chang/CMPUT-401-Winter-2018/blob/master/YCSB%20Report/parsing_output.py
#author: smartDeployer team "https://github.com/yfe3"
#This code is under developing, use this as a demo tool and helper in analysis
# The program can take multiple YCSB output as input generate a plot the show the differnece
# Usage python3 graphicTool.py number_of_file

from matplotlib import pyplot as plt
import sys

total_file_num = 1 #default value
if len(sys.argv) == 2: # get total number of files input
    total_file_num = int(sys.argv[1])

properties_begin = '***************** properties *****************'
properties_end = '**********************************************'
OVERALL = '[OVERALL]'
plot_title = 'Performance Plot'

index_counter = 0 #the counter of total data points we passing

overall_performance_list = [] # list of all data

while index_counter < total_file_num:
    if total_file_num ==1:
        fileName = "workload.txt" #so far need to set a file name but can input systematically later
    else:
        fileName = 'workload'+ str(index_counter+1)+'.txt'
    File = open(fileName,'r')


    Line = File.readlines()

    properties_begin_index = None
    properties_end_index = None
    properties_OVERALL_index = None

    for i in Line:

        if properties_begin in i:
            properties_begin_index = Line.index(i)


        if properties_end in i:
            properties_end_index = Line.index(i)

        if OVERALL in i:
            properties_OVERALL_index = Line.index(i)



    End_Indx = len(Line)
    test_general_info = []

    temp_line = Line[properties_OVERALL_index] # read overall data
    temp_line_split = temp_line.split(",")


    test_report = []


    overall_performance_list.append(temp_line_split[2])
        



    File.close()
    index_counter +=1

plt.plot(overall_performance_list)
print(overall_performance_list)
#print(properties_begin_index,properties_end_index,info_begin_index)
