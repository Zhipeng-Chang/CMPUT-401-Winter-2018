#
#
#
#
#
# note: this script only write the run output

import matplotlib.pyplot as plt

file = open("all_result.txt", 'w')

fileOrder = ['a','b','c','d','e']
for i in range(0,5):
	
	temp_file_name = "workload_run_output"+fileOrder[i]+".txt"
	

	files = open(temp_file_name,"r")
	Line = files.readlines()

	
	OVERALL = '[OVERALL]'
	properties_OVERALL_index = None

	for i in Line:
		if OVERALL in i:
			properties_OVERALL_index = Line.index(i)


	End_Indx = len(Line)
	

	test_general_info = []
	file.write("========================================================\n")
	write_string = "test_output of "+ temp_file_name + " " + fileOrder[i] + '\n' 
	file.write(write_string)
	
	if properties_OVERALL_index != None:
		for i in range(properties_OVERALL_index-1,End_Indx):
			file.write(Line[i]+"\n")


			temp_line = Line[i]
			temp_line_split = temp_line.split(",")

			test_general_info.append(temp_line_split)
