from connect import *


class check:
    def chck(n):
        c = mydb.cursor()
        c.execute("select * from information_schema.tables where table_name = '{}'".format(n))
        try:
            x = list(c.fetchall()[0])
            c.close()
            if n in x:
                return True
            #else:
            #print('f')
            #return False
        except:
            return False
