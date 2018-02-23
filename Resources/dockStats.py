# visualize docker container stats 
# version 0
# this script takes some docker stats from a text file 
# and visualizes them with some graphs  

# author: SmartDeployer Team 

from matplotlib import pyplot as plt 
import sys 


def main():
    # open the stats file 
    filename = sys.argv[1] 
    stats = open(filename)
    
    # parse file for the stats and graph netIO
    data = get_stats(stats)

    #close file 
    stats.close()

def get_stats(filename):
    containers = []
    netIO = []
    for line in filename: 
        # store container_id and netIO in respective arrays
        tmp = line.split([':'])
        containers.append(tmp[0])
        netIO.append(tmp[1])

    # need to decide what to do with the netIO first 
    #plt.plot(netIO)


main()
