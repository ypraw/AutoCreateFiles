###################################
##  Created By Yunindyo Prabowo  ##
##  ypraw@outlook.com            ##
###################################


import mysql.connector
from AutoCreateFiles import *


count = 0
test1 = AutoCreateFiles()
koneksi = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='njajal')
cursor = koneksi.cursor()
query = ("SELECT id_files FROM files ORDER BY id_files DESC LIMIT 0, 1")
cursor.execute(query)

#get value if id_files
for ids in cursor:
    count=ids[0]
#check value id


#id_files equals 0, database is no data
if (count==0):

    while True:
        ts = time.time()
        timestamp = datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        # parsing var count to integer again from string
        # defult type while first loop is integer

        count = int(count)

        if count == 5:      #in reality maybe you need infinite loop / auto run / no limit
            break           #Please delete this block

        count += 1

        # open file
        count = str(count)
        tgl = test1.getDate()
        name = test1.getNames(count, tgl)
        test1.SaveFiles(name)
        # print name
        # ind = re.split('\W+',name)
        ind = name.split("/", 1)
        print ind[1]

        # add Data
        query = ("INSERT INTO files "
                 "(id_files, name_files, time_files) "
                 "VALUES (%s,%s,%s)")
        count = int(count)
        data = (count, ind[1], timestamp)

        cursor.execute(query, data)
        koneksi.commit()

        # auto run every x second
        # for example 1 second
        time.sleep(1)
else:#else next counting from last Id_files

    count = ids[0]  # switching value for next counting in index DB by id_files

    while (True):
        ts = time.time()
        timestamp = datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        count += 1
        # open file
        count = str(count)
        tgl = test1.getDate()
        name = test1.getNames(count, tgl)
        test1.SaveFiles(name)
        # print name
        # ind = re.split('\W+',name)
        ind = name.split("/", 1)
        print ind[1]
        # add Data
        query = ("INSERT INTO files "
                 "(id_files, name_files, time_files) "
                 "VALUES (%s,%s,%s)")
        count = int(count)
        data = (count, ind[1], timestamp)

        cursor.execute(query, data)
        koneksi.commit()

        # every x second
        # for example 1 second
        time.sleep(1)
    print "it's limit"


cursor.close()
koneksi.close()