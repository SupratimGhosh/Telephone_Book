import time
import os
import process as pro1

print("Welcome to TURUCALLER".center(50,'*'))

time.sleep(1)
print('\nPress 1 to login.\nPress 2 to SignUp')
ch1=int(input('Enter your choice: '))
if ch1==1:
    import login
    name=login.login()
    time.sleep(5)
    os.system('cls')
    pro1.process.pro(name)
elif ch1==2:
    import create as cr
    name=cr.create.signup()
    pro1.process.pro(name)

else:
    print('It looks you entered a wrong choice')
    time.sleep(2)
    os.system('cls')
    import execute as e
    e

