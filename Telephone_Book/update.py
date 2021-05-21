from connect import *

class update:

    def upd(name):
        cursor = mydb.cursor()
        n=input('Enter the contact to be updated: ')
        q = 'select * from {} where name="{}"'.format(name, n)
        try:
            cursor.execute(q)
            result = cursor.fetchall()
            # for i in result:
            print(result)
            NE=list(result[0])
            N,NM,AD=NE[0],NE[1],NE[2]

            print('Press 1 to change the Name.\nPress 2 to change the Number.\nPress 3 to Update Address.\n')
            choice=int(input('Enter the choice: '))

            if choice==1:
                newName=input('Enter the new Name: ')
                q1 = 'UPDATE {} SET name="{}" Where name="{}"'.format(name, newName, N)
                N=newName
                query='Name'
            elif choice==2:
                newNum=input('Enter the new Number: ')
                q1='UPDATE {} SET number="{}" Where number="{}"'.format(name,newNum,NM)
                query = 'Number'
            elif choice==3:
                newAdd=input('Enter the new Address: ')
                q1 = 'UPDATE {} SET address="{}" Where address="{}"'.format(name, newAdd, AD)
                query = 'Address'
            else:
                print('You Entered a wrong choice!')
                query = 'Nothing'
                return

            try:
                cursor.execute(q1)
                print(query,' Updated!')
                mydb.commit()
                q = 'select * from {} where name="{}"'.format(name, N)
                cursor.execute(q)
                result = cursor.fetchall()
                print(result)
            except:
                print("You entered a wrong {}!".format(query))
        except:
            print('No such contact found!')