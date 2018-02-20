
import mysql.connector
import sys

developmentMode = True


def drop_table():
	#this function will be invoke only if the development mode is on
	
	cursor.execute("drop table if exists CLEANUP;")
	cursor.execute("drop table if exists INSERTS;")
	cursor.execute("drop table if exists UPDATES;")
	cursor.execute("drop table if exists READSS;")
	cursor.execute("drop table if exists SCAN;")
	cursor.execute("drop table if exists TOTAL;")
	cursor.execute("drop table if exists container_system;")


def container_system(cpu,memory,blockio,testid):

	cursor.execute("create table if not exists container_system (testID char(20),\
					CPU float, Memory char(20), BlockIO integer, \
					primary key(testID));")
	cursor.execute("insert into container_system (testID,\
					CPU, Memory, BlockIO) values (%s,%s,%s,%s)",(testid,cpu,memory,blockio))

def TOTAL(total_data,workload):
	
	only_num = []
	for i in total_data:
		if "[TOTAL" in i or "[OVERALL]" in i:
			data = i.split(",")
			data_length = len(data)
			tem_num = data[data_length-1].replace("\n","")
			only_num.append(tem_num)

	cursor.execute("create table if not exists TOTAL (testID char(20), workload char(5), RunTime_ms float, \
	                Throughput float, TOTAL_GCS_PS_Scavenge float, \
	                TOTAL_GC_TIME_PS_Scavenge_ms float,\
	                TOTAL_GC_TIME_PS_Scavenge_per float,\
	                TOTAL_GCS_PS_MarkSweep float,\
	                TOTAL_GC_TIME_PS_MarkSweep_ms float,\
	                TOTAL_GC_TIME_PS_MarkSweep_per float,\
	                TOTAL_GCs float, TOTAL_GC_TIME_ms float,\
	                TOTAL_GC_TIME_per float); ")

	cursor.execute("ALTER TABLE TOTAL ADD FOREIGN KEY TOTAL(testID) REFERENCES container_system(testID)\
					ON DELETE NO ACTION ON UPDATE CASCADE;")
	# cursor.execute("insert into CLEANUP values (%s,%s,%f,%f,%f,%f,%f,%f)",(testID,))


def CLEANUP(cleanup_data,workload):

	# cleanup_data is a list with all [CLEAN]
	only_num = []
	for i in cleanup_data:
		data = i.split(",")
		data_length = len(data)
		tem_num = data[data_length-1].replace("\n","")
		only_num.append(tem_num)



	cursor.execute("create table if not exists CLEANUP (testID char(20), workdload char(5) Operations float,\
	                AverageLatency float, MinLatency float, MaxLatency float,\
	                95thPercentileLatency float, 99thPercentileLatency float);")
	cursor.execute("ALTER TABLE CLEANUP ADD FOREIGN KEY CLEANUP(testID) REFERENCES container_system(testID)\
	                ON DELETE NO ACTION ON UPDATE CASCADE;")
	# cursor.execute("insert into CLEANUP values (%s,%s,%f,%f,%f,%f,%f,%f)",(testID,))


def INSERT(insert_data,workload):
	cursor.execute("create table if not exists INSERTS (testID char(20), Operations float,\
	                AverageLatency float, MinLatency float, MaxLatency float,\
	                95thPercentileLatency float, 99thPercentileLatency float);")
	cursor.execute("ALTER TABLE INSERTS ADD FOREIGN KEY INSERTS(testID) REFERENCES container_system(testID) \
	                ON DELETE NO ACTION ON UPDATE CASCADE;")

def SCAN(scan_data,workload):
	cursor.execute("create table if not exists SCAN (testID char(20), Operations float,\
	                AverageLatency float, MinLatency float, MaxLatency float,\
	                95thPercentileLatency float, 99thPercentileLatency float);")
	cursor.execute("ALTER TABLE SCAN ADD FOREIGN KEY SCAN(testID) REFERENCES container_system(testID) \
	                ON DELETE NO ACTION ON UPDATE CASCADE;")


#this parsing give correct list
def READ(read_data,workload):
	only_num = []
	for i in read_data:
		data = i.split(",")
		data_length = len(data)
		tem_num = data[data_length-1].replace("\n","")
		only_num.append(tem_num)

	cursor.execute("create table if not exists READSS (testID char(20), Operations FLOAT(10,10),\
	                AverageLatency FLOAT(10,10), MinLatency FLOAT(10,10), MaxLatency FLOAT(10,10),\
	                95thPercentileLatency FLOAT(10,10), 99thPercentileLatency FLOAT(10,10));")
	cursor.execute("ALTER TABLE READSS ADD FOREIGN KEY READSS(testID) REFERENCES container_system(testID) \
	                ON DELETE NO ACTION ON UPDATE CASCADE;")



def UPDATE(update_data,workload):
	cursor.execute("create table if not exists UPDATES (testID char(20), Operations float,\
	                AverageLatency float, MinLatency float, MaxLatency float,\
	                95thPercentileLatency float, 99thPercentileLatency float);")
	cursor.execute("ALTER TABLE UPDATES ADD FOREIGN KEY UPDATES(testID) REFERENCES container_system(testID) \
	                ON DELETE NO ACTION ON UPDATE CASCADE;")





def commit_data(data):
	buffers = data[0].split(" ")
	workload = buffers[len(buffers)-1]
	read = []
	scan = []
	cleanup = []
	update = []
	insert = []
	total = []
	for i in data:
		if "[READ]" in i:
			read.append(i)
		elif "[CLEANUP]" in i:
			cleanup.append(i)
		elif "[UPDATE]" in i:
			update.append(i)
		elif "[INSERT]" in i:
			insert.append(i)
		elif "[SCAN]" in i:
			scan.append(i)
		else:
			total.append(i)
	if len(read) != 0:
		print("read not empty")
		READ(read,workload)
	if len(scan) != 0:
		print("scan not empty")
		SCAN(scan,workload)
	if len(cleanup) != 0:
		print("cleanup not empty")
		CLEANUP(cleanup,workload)
	if len(update) != 0:
		print("update not empty")
		UPDATE(update,workload)
	if len(insert) != 0:
		print("insert not empty")
		INSERT(insert,workload)
	if len(total) != 0:
		print("total not empty")
		TOTAL(total,workload)
	

# add_ycsb_report_data = ("insert into ycsb() values (?,?,?,?,?,?)" )

# cursor.execute(add_ycsb_report_data,report_data)


def main():

	outputFile = open("all_result.txt")
	outputFiles = outputFile.readlines()
	global testID
	global cursor
	#container system input
	memory = sys.argv[1]
	cpu    = float(sys.argv[2])
	blkio  = int(sys.argv[3])
	testID = memory + str(cpu) + str(blkio)

	


	try:
	    db = mysql.connector.connect(user='root', password='password',host='162.246.156.220',database='smartdeployer')
	except mysql.connector.Error as err:
	    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
	        print("Something is wrong with your user name or password")
	    elif err.errno == errorcode.ER_BAD_DB_ERROR:
	        print("Database does not exist")
	    else:
	        print(err)

	cursor = db.cursor()


	if developmentMode == True:
		drop_table()


	
	container_system(cpu,memory,blkio,testID)

	index = 0
	indexs = []
	data = []
	while (index<len(outputFiles)):
		if "========================================================" in outputFiles[index]:
			indexs.append(index)
		index += 1
	for i in range(0,len(indexs)):
		first_index = indexs[i]
		second_index = indexs[i+1]
		for i in range(first_index+1,second_index-1):
			data.append(outputFiles[i])
		commit_data(data)
		sys.exit(0)
		data.clear()


	db.commit()
	cursor.close()
	db.close()


if __name__ == "__main__":
	main()


