print("--------------------              PC EXPRESS            ---------------------")
print('\n')
print("--------------------             DATABASE 2020          ---------------------")
print("\n")

def menu():
    c='y'
    while(c=='y'):
        print('1.PC Component')
        print('2.Sales Detail')
        print('3.Exit')
        print('\n')
        choice=int(input('Enter the number:'))
        print('\n')
        if choice==1:
            print('1.Motherboard')
            print('2.Processor')
            print('3.Ram')
            print('4.Storage')
            print('5.Graphic card')
            print('6.Power Supply')
            print('7.Cabinet')
            print('8.EXIT')
            print('\n')
            a=int(input('Enter the number:'))
            print('\n')
            if a==1:
                print('1.Add Motherboard Record')
                print('2.Update Motherboard Record')
                print('3.Display Motherboard Record')
                print('4.Modify Motherboard Record')
                print('5.Delete Record from table')
                print('6.Main Menu')
                print('\n')
                x=int(input('Enter the number'))
                if x==1:
                    addmb()
                elif x==2:
                    upmb()
                elif x==3:
                    dismb()
                elif x==4:
                    modmb()
                elif x==5:
                    delmb()
                else :
                    print('Returning to main menu')
def addmb():
    import mysql.connector
    mydb=mysql.connector.connect(host='localhost',user='root',passwd="",db="pc_express")
    mycursor=mydb.cursor()
    name=input('Model Name:')
    company=input('Company Name:')
    soctype=input("socket_type Name:")
    chip=input('Chipset Name:')
    qty=input('QUANTITY:')
    price=input('Enter Price:')
    mycursor.execute("""INSERT INTO motherboard(Name,Company,Socket_type,Chipset,Qty,Price)VALUES(%s,%s,%s,%s,%s,%s)""",(name,company,soctype,chip,qty,price))
    mydb.commit()
    print("Done")

def upmb():
    import mysql.connector
    try:
        mydb=mysql.connector.connect(host='localhost',user='root',passwd="",db="pc_express")
        mycursor=mydb.cursor()
        U=input("Enter the SQL Command for update:")
        mycursor.execute(U)
        mydb.commit()
        print('Record Updated')

    except Exception as e:
        print(e)

def dismb():
    import mysql.connector
    try:
        mydb=mysql.connector.connect(host='localhost',user='root',passwd="",db="pc_express")
        mycursor=mydb.cursor()
        D=input("enter the statement to Fetch from table ")
        mycursor.execute(D)
        print("Data Displayed")
        mydb.commit()
    except:
        print("Error:unable to fetch data.Please try again")
def modmb():
    import mysql.connector
    try:
        mydb=mysql.connector.connect(host='localhost',user='root',passwd="",db="pc_express")
        mycursor=mydb.cursor()
        w=input("Enter the Sql Command:")
        mycursor.execute(w)
        mydb.commit()
        print("Table is Modified")
    except Exception as e:
        print(e)
        print("Unable to Modify")

def delmb():
    import mysql.connector
    try:
        mydb=mysql.connector.connect(host='localhost',user='root',passwd="",db="pc_express")
        mycursor=mydb.cursor()
        r=input("Enter The sql command:")
        mycursor.execute(r)
        mydb.commit()
        print("Record Deleted")
    except Exception as e:
        print(e)
        print("Unable to delete")

menu()


        












