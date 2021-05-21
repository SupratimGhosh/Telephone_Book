
from connect import *

class search():
    def search(name):
            csr = mydb.cursor()
            print('\nPress 1 to search for a particular name.')
            print('Press 2 to see full contact list')
            inp=int(input('Enter your choice: '))
            if inp==1:
                sname=input('Enter the Name to be searched: ')
                q='select * from {} where name="{}"'.format(name,sname)
                try:
                    csr.execute(q)
                    result=csr.fetchall()
                    for i in result:
                        print(i)
                except:
                    print('No such contact found!')
            elif inp==2:
                q="select * from {} order by name".format(name)
                csr.execute(q)
                res=csr.fetchall()
                print()
                print('Name\t\t\tNumber\t\t\tAddress')
                for i in res:
                    NE = list(i)
                    N, NM, AD = NE[0], NE[1], NE[2]
                    print(N,'\t\t',NM,'\t\t',AD)

            else:
                print('Sorry! You entered a wrong choice!')

