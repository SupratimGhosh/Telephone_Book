from connect import *


class exe:
    cursor = mydb.cursor()
    cursor.execute('show tables')

    for i in cursor:
     print(i)