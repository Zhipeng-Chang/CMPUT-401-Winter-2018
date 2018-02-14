#
#
#
#
#


fileName = open("hostIP.txt","r")
fileContent = fileName.readlines()

file_length = len(fileContent)

last_len = fileContent[file_length-1].split(" ")
IP = last_len[2]
print(IP)
