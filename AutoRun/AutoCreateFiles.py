###################################
##  Created By Yunindyo Prabowo  ##
##  ypraw@outlook.com            ##
###################################


import time
from datetime import datetime
import re


class AutoCreateFiles:

    """get current time when this script runnin"""""
    def getDate(self):
        self.times = datetime.now().strftime('%Y%m%d-%H%M%S')
        return self.times

    """ return Name newfile_numberOfFile-currentTime.txt"""
    def getNames(self,count,times):
        self.names = "files/newFile_" + count + "-" + times + ".txt"
        return self.names

    """ save file to directory""" ""
    def SaveFiles(self, names):
        self.file = open(names, 'w')
        self.file.write("hello")
        self.file.close()
        return self.file



if __name__ == '__main__':
    count =0
    test1 = AutoCreateFiles()
    while True:

        #parsing var count to integer again from string
        #defult type while first loop is integer
        count = int(count)
        if count==5:
            break
        count+=1

        #open file
        count=str(count)
        tgl = test1.getDate()
        name = test1.getNames(count,tgl)
        test1.SaveFiles(name)
        print name
        #ind = re.split('\W+',name)
        ind = name.split("/",1)
        print ind[1]

        # every x second
        # for example 1 second
        time.sleep(1)