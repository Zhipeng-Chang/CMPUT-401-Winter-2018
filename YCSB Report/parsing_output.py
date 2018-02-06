#For visualize the output of ycsb report
#version 1.0  final verison
#author: Xuan Cao "https://github.com/Danissss"


fileName = "workload.txt"
File = open(fileName,'r')
Line = File.readlines()
properties_begin = '***************** properties *****************'
properties_end = '**********************************************'
OVERALL = '[OVERALL]'




#print(type(Line)) : Line is list
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

if properties_begin_index != None:
    for i in range(properties_begin_index+1, properties_end_index):
    
        temp_line = Line[i]
        temp_line_split = temp_line.split("=")
        test_general_info.append(temp_line_split)

test_report = []
if properties_OVERALL_index != None:
    for i in range(properties_OVERALL_index-1,End_Indx):
        temp_line = Line[i]
        temp_line_split = temp_line.split(",")

        test_report.append(temp_line_split)
        
print("Testing Information:")
print("====================================================================================")
for i in test_general_info:
    print("{: <30} {: <30} ".format(*i))
   
    # for j in range(len(test_general_info[i])):
    #     print(test_general_info[i][j])

print("====================================================================================")

print("Testing Report: \n")
print("====================================================================================")
print("|Action                        |Parameters                    |Values      |")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
for i in test_report:
    print("{: <30} {: <30} {: <30}".format(*i))
   

    # for j in range(len(i)):
    #     print(i[j])
    # for j in range(len(i)):
    #     print(Line[i][j])




#print(properties_begin_index,properties_end_index,info_begin_index)