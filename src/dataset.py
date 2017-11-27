from decimal import *


def readData():
    rawData = open('../Dataset/u_c_hihi.0', 'r')
    auxList = rawData.readlines()
    # After readlines is called, each number will a string appended by a \n
    myList = []
    for i in auxList:
        myList.append(i.strip())
    # \n is removed now

    myList = [Decimal(x) for x in myList]
    # converted the string to decimal as it gives precise results
    tasks = []
    for i in range(0, len(myList), 16):
        tasks.append(myList[i:i + 16])
    """ 
        split the list into a nested list
        tasks[i] has the list of running times of ith task on all processors
        extract tasks[i][j] to find running time of task i on processor j
    """
    rawData.close()
    return tasks
