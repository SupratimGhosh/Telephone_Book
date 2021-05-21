import connect

class process:
    def __init__(self):
        pass

    def ph():
        print("Welcome to TURUCALLER".center(50,'*'))
        # process.pro()

    def pro(name):
        import time, os
        process.ph()
        print('Press 0 to search for a contact')
        print('Press 1 to Insert a contact')
        print('Press 2 to Update a contact')
        print('Press 3 to Delete a contact')
        print('Just Press \'Enter\' to Exit')
        try:
            ch=int(input('\nEnter your choice: '))
            if ch==1:
                import insert as ins
                ins.insert.insert(name)
                time.sleep(3)
                os.system('cls')
                process.pro(name)

            elif ch==2:
                import update as up
                up.update.upd(name)
                time.sleep(3)
                os.system('cls')
                process.pro(name)

            elif ch==3:
                import delete as d
                d.delt.dlt(name)
                time.sleep(3)
                os.system('cls')
                process.pro(name)

            elif ch==0:
                import search as sr
                sr.search.search(name)
                x=input('\n\nPress Enter to continue:')
                time.sleep(3)
                os.system('cls')
                process.pro(name)

            else:
                pass
        except:
            print('Thanks for Using TURUCALLER')
            time.sleep(10)