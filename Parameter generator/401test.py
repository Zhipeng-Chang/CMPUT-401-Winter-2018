#!/usr/bin/env python
#import matplotlib.pyplot as plt
from __future__ import division

import numpy as np
import math
# Read below!!!

# Since this code is still a blueprint, so there is not much comment on it
# I will talk about this on Fri with client and see if this approach works
# If yes, I will add more comment and will make the code nicer 


# Read above!!!
GROUPS = ["0-100","101-200","201-300","301-400","401-500","501-600","601-700","701-800","801-900","901-1000"]
GAP = 100

if __name__ == "__main__":
    
    f=open("401test.txt","r")
    lines=f.readlines()
    mydict={}
        
    times=[]
    results = []
    num_of_para = len(lines[0].split('\t'))
    for i in range(len(GROUPS)):
        results.append([GROUPS[i]])
    for single_result in lines:
        final_time = single_result.split('\t')[num_of_para-1].strip('\n')
        times.append (final_time)
        mydict[final_time] = []
        for j in range(num_of_para-1):
            mydict[final_time].append(single_result.split('\t')[j])
    total_num = len(times) #total number of the sample 
    
    # put sample into different groups 
    for i in range(len(GROUPS)):
        for time in times:
            time = int(time)
            if time<i*GAP+GAP and time> i*GAP+1:
                results[i].append(time)
                
    # All code below are calculating each setting's percentage for each group
                
    all_result = []   
    for group_index in range(len(GROUPS)):
        all_result.append([results[group_index][0]])
        
        single_group_all_result = []
        for setting_index in range(num_of_para-1):
            single_group_all_result.append(["setting"+str(setting_index)])
            
            single_group_single_result=[]
            settings_with_duplicated=[]
            for result_index in range(1,len(results[group_index])):
                result=mydict.get(str(results[group_index][result_index]))[setting_index]
                settings_with_duplicated.append(result)
                
            for setting in settings_with_duplicated:
                if setting not in single_group_single_result:
                    single_group_single_result.append(setting)
                    single_group_single_result.append([str(round((settings_with_duplicated.count(setting)/total_num)*100,2))+"%"])
                    
            single_group_all_result[setting_index].append(single_group_single_result)
            
        all_result[group_index].append(single_group_all_result)

    # Print out the result 
    for each_group in all_result:
        print "Group",each_group[0]
        for all_setting in each_group[1:]:
            for each_setting in all_setting:
                print each_setting   
    
    f.close()    
