from connect import *

class create:
    def signup():
        cursor=mydb.cursor()

        sql='CREATE TABLE {} (name VARCHAR(255), number VARCHAR(255), address VARCHAR(255))'
        table=input('Enter your Username: ')
        sql=sql.format(table)

        cursor.execute(sql)

        print('Telephone Directory created by the name: ',table)
        import time; time.sleep(3)
        import os; os.system('cls')
        return table