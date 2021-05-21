# from check import check
from connect import *

class insert:
    def insert(name):
        cursor = mydb.cursor()

    # name = input("Enter your username (name of directory): ")
    # ch=check.chck(name)
        print('Directory opened!')
        while True:
            n = input('Name of the person: ')
            num = input('Number of the person: ')
            add = input('Address of the person: ')

            #sql = 'insert into {} (name,number,address) values (%s,%s,%s)'.format(name)
            val = [n, num, add]

            cursor.execute('insert into {} (name,number,address) values (%s,%s,%s)'.format(name), val)

            print("Number added! ")
            ch = input('Do you want to add more numbers? y/n: ')
            if ch == ('y' or 'Y'):
                continue
            else:
                break

        mydb.commit()
        print('Great! All the entered numbers were added to the phonebook.')