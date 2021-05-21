from check import *
from load import *

def login():
    name = input('Enter the username: ')
    ch = check.chck(name.lower())
    loading.load()
    if ch:
        print('Directory opened!')
        return name
    else:
        print('It looks like You don\'t have an Pre-existing Directory')
        x=input('Please press "Enter" to Create a New one!')
        import create
        create.create.signup()

