from connect import *

class delt:
    def dlt(name):
        cursor = mydb.cursor()
        n=input('Enter the contact name to be deleted: ')
        q='delete from {} where name="{}"'.format(name,n)
        try:
            cursor.execute(q)
            mydb.commit()
            print('Contact deleted!')
        except:
            print('No such contact found!')
