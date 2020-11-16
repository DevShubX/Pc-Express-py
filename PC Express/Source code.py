print("--------------------              PC EXPRESS            ---------------------")
print('\n')
print("--------------------             DATABASE 2020          ---------------------")
print("\n")

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
                def mob():            
                    c='y'
                    while c=='y':
                        print('1.Add Motherboard Record')
                        print('2.Update Motherboard Record')
                        print('3.Display Motherboard Record')
                        print('4.Modify Motherboard Record')
                        print('5.Delete Motherboard Record')
                        print('6.Main Menu')
                        print('\n')
                        x=int(input('Enter the number:'))
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
                            break
                        
                def addmb():
                    import mysql.connector
                    try:
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
                        print("Record Inserted")
                    except Exception as e:
                        print("Unable to insert record")
                        print(e)
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
                        print("Unable to update record")
                def dismb():
                    import mysql.connector
                    try:
                        mydb=mysql.connector.connect(host='localhost',user='root',passwd="",db="pc_express")
                        mycursor=mydb.cursor()
                        d=input("Enter SQL Command for displaying record:")
                        mycursor.execute(d)
                        results=mycursor.fetchall()
                        for i in results:
                            print(i)
                        print("Record Displayed")
                        mydb.commit()
                    except Exception as e:
                        print("Error:unable to fetch data.Please try again")
                        print(e)
                def modmb():
                    import mysql.connector
                    try:
                        mydb=mysql.connector.connect(host='localhost',user='root',passwd="",db="pc_express")
                        mycursor=mydb.cursor()
                        w=input("Enter the Sql Command:")
                        mycursor.execute(w)
                        mydb.commit()
                        print("Record Modified")
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
                mob()
            if a==2:
                def pro():
                    print("1.Add Processsor Records")
                    print("2.Update Processor Records")
                    print('3.Display Proecessor Records')
                    print("4.Modify Processor Records")
                    print("5.Delete Processor Records")
                    print('6.Exit')
                    print('\n')
                    t=int(input("Enter Your Choice:"))
                    print('\n')
                    if t==1:
                        addpro()
                    elif t==2:
                        uppro()
                    elif t==3:
                        dispro()
                    elif t==4:
                        modpro()
                    elif t==5:
                        delpro()
                    else:
                        ('Returning to main menu...')
                def addpro():
                    import mysql.connector
                    try:
                        mydb=mysql.connector.connect(host='localhost',user='root',passwd="",db='pc_express')
                        mycursor=mydb.cursor()
                        company=input('Enter company name:')
                        name=input('Enter Product name:')
                        cores=int(input('Enter No of cores:'))
                        soctype=input("Enter soctype:")
                        basecl=input('Enter base clock:')
                        boostcl=input("Enter Boost clock:")
                        qty=input('Enter Quantity:')
                        price=input('Enter price:')
                        mycursor.execute("""INSERT INTO processor(Company,Name,Cores,Socket_type,Base_clock,Boost_clock,Qty,Price)VALUES(%s,%s,%s,%s,%s,%s,%s,%s)""",(company,name,cores,soctype,basecl,boostcl,qty,price))
                        mydb.commit()
                        print('Records Inserted')
                    except Exception as e:
                        print("Unable to insert record")
                        print(e)
                
                def uppro():
                    import mysql.connector
                    try:
                        mydb=mysql.connector.connect(host='localhost',user='root',passwd="",db='pc_express')
                        mycursor=mydb.cursor()
                        u=input('Enter SQL Command for update:')
                        mycursor.execute(u)
                        print("Record updated")
                        mydb.commit()
                    except Exception as e:
                        print(e)
                        print('Unable to Update record')

                def dispro():
                    import mysql.connector
                    try:
                        mydb=mysql.connector.connect(host='localhost',user='root',passwd="",db='pc_express')
                        mycursor=mydb.cursor()
                        d=input("Enter the SQL command for displaying Record")
                        mycursor.execute(d)
                        results=mycursor.fetchall()
                        for o in results:
                            print(o)
                        print("Displaying Record...")
                        mydb.commit()
                    except Exception as e:
                        print(e)
                        print('Unable to display record')
                
                def modpro():
                    import mysql.connector
                    try:
                        mydb=mysql.connector.connect(host='localhost',uer='root',passwd="",db='pc_express')
                        mycursor=mydb.cursor()
                        m=input("Enter SQL Command for modifiying Record" )
                        mycursor.execute(m)
                        print("Record Modified")
                        mydb.commit()
                    except Exception as e:
                        print(e)
                        print("Unable to modify record")

                def delpro():
                    import mysql.connector
                    try:
                        mydb=mysql.connector.connect(host='localhost',user='root',pssswd="",db='pc_express')
                        mycursor=mydb.cursor()
                        k=input("Enter SQL Command for Deleting Record")
                        mycursor.execute(k)
                        print('Record deleted')
                        mydb.commit()
                    except Exception as e:
                        print('Unable to delete Record')
                        print(e)                        
                pro()
            if a==3:
                def ram():
                    print("1.Add Ram Records")
                    print("2.Update Ram Records")
                    print("3.Display Ram Records")
                    print("4.Modify Ram Records")
                    print("5.Delete Ram Records")
                    print("6.Exit")
                    print("\n")
                    x=int(input("Enter Your choice:"))
                    print('\n')
                    if x==1:
                        addram()
                    elif x==2:
                        upram()
                    elif x==3:
                        disram()
                    elif x==4:
                        modram()
                    elif x==5:
                        delram()
                    else:
                        print("Returing to main menu...")

                def addram():
                    import mysql.connector
                    try:
                        mydb=mysql.connector.connect(host='localhost',user='root',passwd="",db='pc_express')
                        mycursor=mydb.cursor()
                        company=input("Enter Company name:")
                        name=input('Enter Name:')
                        size=input("Enter Size:")
                        speed=input('Enter Speed:')
                        ramtype=input("Enter Ramtype:")
                        qty=input('Enter Quantity:')
                        price=input('Enter Price:')
                        mycursor.execute("""INSERT INTO rams(Company,Name,Size,Speed,Ram_type,Qty,Price)VALUES(%s,%s,%s,%s,%s,%s,%s)""",(company,name,size,speed,ramtype,qty,price))
                        print('Record Inserted')
                        mydb.commit()
                    except Exception as e:
                        print("Unable to insert Record")
                        print(e)
                
                def upram():
                    import mysql.connector
                    try:
                        mydb=mysql.connector.connect(host='localhost',user='root',passwd="",db='pc_express')
                        mycursor=mydb.cursor()
                        u=input("Enter SQL Command for update:")
                        mycursor.execute(u)
                        print('Record updated')
                        mydb.commit()
                    except Exception as e:
                        print("Unable to update record")
                        print(e)
                def disram():
                    import mysql.connector
                    try:
                        mydb=mysql.connector.connect(host='localhost',user='root',passwd="",db='pc_express')
                        mycursor=mydb.cursor()
                        g=input("Enter SQL Command for displaying record:")
                        mycursor.execute(g)
                        results=mycursor.fetchall()
                        for j in results:
                            print(j)
                        print('Record Displayed')
                        mydb.commit()
                    except Exception as e:
                        print("Unable to display record")
                        print(e)
                def modram():
                    import mysql.connector
                    try:
                        mydb=mysql.connector.connect(host='localhost',user='root',passwd="",db='pc_express')
                        mycursor=mydb.cursor()
                        h=input('Enter SQL Command for modifying record:')
                        mycursor.execute(h)
                        print('Record modified')
                        mydb.commit()
                    except Exception as e:
                        print("Unable to modify record")
                        print(e)
                def delram():
                    import mysql.connector
                    try:
                        mydb=mysql.connector.connect(host='localhost',user='root',passwd="",db='pc_express')
                        mycursor=mydb.cursor()
                        j=input('Enter the SQL Command for delete')
                        mycursor.execute(j)
                        print('Record deleted')
                        mydb.commit()
                    except Exception as e:
                        print("Unable to delete")
                        print(e)
                ram()
            if a==4:
                def storage():
                    print("1.Add Storage Records")
                    print("2.Update Storage Records")
                    print("3.Display Storage Records")
                    print("4.Modify Storage Records")
                    print("5.Delete Storage Records")
                    print("6.Exit")
                    print("\n")
                    c=int(input("Enter Your Choice:"))
                    print('\n')
                    if c==1:
                        addsto()
                    elif c==2:
                        upsto()
                    elif c==3:
                        dissto()
                    elif c==4:
                        modsto()
                    elif c==5:
                        delsto()
                    else:
                        print("Returing to main menu...")
                def addsto():
                    import mysql.connector
                    try:
                        mydb=mysql.connector.connect(host='localhost',user='root',passwd="",db='pc_express')
                        mycursor=mydb.cursor()
                        company=input('Enter Company name:')
                        name=input('Enter product name:')
                        type=input('Enter storage type:')
                        speed=input('Enter speed:')
                        size=input("Enter Storage size:")
                        qty=input('Enter Quantity')
                        price=input('Enter price:')
                        mycursor.execute("""INSERT INTO storage(Company,Name,Type,Speed,Size,Qty,Price)VALUES(%s,%s,%s,%s,%s,%s,%s)""",(company,name,type,speed,size,qty,price))
                        print('Record Inserted')
                        mydb.commit()
                    except Exception as e:
                        print("Unable to insert record ")
                        print(e)
                def upsto():
                    import mysql.connector
                    try:
                        mydb=mysql.connector.connect(host='localhost',user='root',passwd="",db="pc_express")
                        mycursor=mydb.cursor()
                        z=input("Enter the SQL Command for update:")
                        mycursor.execute(z)
                        print('Record Updated')
                        mydb.commit()
                    except Exception as e:
                        print("Unable to update the record")
                        print(e)
                def dissto():
                    import mysql.connector
                    try:
                        mydb=mysql.connector.connect(host='localhost',user='root',passwd="",db="pc_express")
                        mycursor=mydb.cursor()
                        v=input("Enter SQL Command for displaying record:")
                        mycursor.execute(v)
                        results=mycursor.fetchall()
                        for n in results:
                            print(n)
                        print('Record Displayed')
                        mydb.commit()
                    except Exception as e:
                        print("Unable to display record")
                        print(e)
                def modsto():
                    import mysql.connector
                    try:
                        mydb=mysql.connector.connect(host='localhost',user='root',passwd="",db='pc_express')
                        mycursor=mydb.cursor()
                        b=input("Enter SQL Command for Modify:")
                        mycursor.execute(b)
                        print('Record Modified')
                        mydb.commit()
                    except Exception as e:
                        print("Unable to modify record")
                        print(e)
                def delsto():
                    import mysql.connector
                    try:
                        mydb=mysql.connector.connect(host='localhost',user='root',passwd="",db='pc_express')
                        mycursor=mydb.cursor()
                        n=input("Enter SQL Command for deleting Records:")
                        mycursor.execute(n)
                        print("Records Deleted")
                        mydb.commit()
                    except Exception as e:
                        print("Unable to Delete record")
                        print(e)
                storage()
            if a==5:
                def gfx():
                    print("1.Add Graphic card Records")
                    print("2.Update Graphic card Records")
                    print("3.Display Graphic card Records")
                    print("4.Modify Graphic card Records")
                    print("5.Delete Graphic card Records")
                    print("6.Exit")
                    print('\n')
                    y=int(input('Enter Your Choice:'))
                    print('\n')
                    if y==1:
                        addgfx()
                    elif y==2:
                        upgfx()
                    elif y==3:
                        disgfx()
                    elif y==4:
                        modgfx()
                    elif y==5:
                        delgfx()
                    else:
                        print('Returing to main menu...')

                def addgfx():
                    import mysql.connector
                    try:
                        mydb=mysql.connector.connect(host='localhost',user='root',passwd="",db='pc_express')
                        mycursor=mydb.cursor()
                        company=input("Enter company name:")
                        name=input("Enter product name:")
                        memtype=input("Enter Memory Type:")
                        vram=input("Enter Amount of vram:")
                        qty=input('Enter Quantity')
                        price=input("Enter price of graphic card")
                        mycursor.execute("""INSERT INTO graphic_cards(Company,Name,Memory_Type,Vram,Qty,Price)VALUES(%s,%s,%s,%s,%s,%s)""",(company,name,memtype,vram,qty,price))
                        print("Record Inserted")
                        mydb.commit()
                    except Exception as e:
                        print("Unable to insert record")
                        print(e)
                def upgfx():
                    import mysql.connector
                    try:
                        mydb=mysql.connector.connect(host='localhost',user='root',passwd="",db='pc_express')
                        mycursor=mydb.cursor()
                        i=input('Enter SQL Command for updating records:')
                        mycursor.execute(i)
                        print("Record Updated")
                        mydb.commit()
                    except Exception as e:
                        print("Unable to update records")
                        print(e)
                def disgfx():
                    import mysql.connector
                    try:
                        mydb=mysql.connector.connect(host='localhost',user='root',passwd="",db='pc_express')
                        mycursor=mydb.cursor()
                        r=input('Enter SQL Command for displaying record:')
                        mycursor.execute(r)
                        results=mycursor.fetchall()
                        for k in results:
                            print(k)
                        print('Record Displayed')
                        mydb.commit()
                    except Exception as e:
                        print("Unable to display records")
                        print(e)
                def modgfx():
                    import mysql.connector
                    try:
                        mydb=mysql.connector.connect(host='localhost',user='root',passwd="",db='pc_express')
                        mycursor=mydb.cursor()
                        o=input('Enter the SQL Command for modifying record:')
                        mycursor.execute(o)
                        print("Record Modified")
                        mydb.commit()
                    except Exception as e:
                        print("Unable to modify record")
                        print(e)
                def delgfx():
                    import mysql.connector
                    try:
                        mydb=mysql.connector.connect(host='localhost',user='root',passwd="",db='pc_express')
                        mycursor=mydb.cursor()
                        u=input('Enter the SQL Command for deleting records:')
                        mycursor.execute(u)
                        print("Record deleted")
                        mydb.commit()
                    except Exception as e:
                        print("Unable to delete record")
                        print(e)
                gfx()
            if a==6:
                def psu():
                    print("1.Add Power Supply Records")
                    print("2.Update Power Supply Records")
                    print("3.Display Power Supply Records")
                    print("4.Modify Power Supply Records")
                    print("5.Delete Power Supply Records")
                    print('\n')
                    e=int(input('Enter Your Choice:'))
                    print('\n')
                    if e==1:
                        addpsu()
                    elif e==2:
                        uppsu()
                    elif e==3:
                        dispsu()
                    elif e==4:
                        modpsu()
                    elif e==5:
                        delpsu()
                    else:
                        print("Returing to main menu...")
                def addpsu():
                    import mysql.connector
                    try:
                        mydb=mysql.connector.connect(host='localhost',user='root',passwd="",db='pc_express')
                        mycursor=mydb.cursor()
                        company=input('Enter Company name:')
                        name=input('Enter Product name:')
                        psutype=input('Enter the psu type:')
                        watts=input('Enter Watts: ')
                        qty=input('Enter Quantity:')
                        price=input('Enter price:')
                        mycursor.execute("""INSERT INTO power_supply(Company,Name,Type,Watts,Qty,Price)VALUES(%s,%s,%s,%s,%s,%s)""",(company,name,psutype,watts,qty,price))
                        print("Record Inserted")
                        mydb.commit()
                    except Exception as e:
                        print('Unable to insert record')
                        print(e)
                def uppsu():
                    import mysql.connector
                    try:
                        mydb=mysql.connector.connect(host='localhost',user='root',passwd="",db='pc_express')
                        mycursor=mydb.cursor()
                        s=input("Enter SQL Command for update:")
                        mycursor.execute(s)
                        print("Record updates")
                        mydb.commit()
                    except Exception as e:
                        print('Unable to insert record')
                        print(e)
                def dispsu():
                    import mysql.connector
                    try:
                        mydb=mysql.connector.connect(host='localhost',user='root',passwd="",db='pc_express')
                        mycursor=mydb.cursor()
                        d=input("Enter SQL Command for displaying records:")
                        mycursor.execute(d)
                        results=mycursor.fetchall()
                        for l in results:
                            print(l)
                        print("Records Displayed")
                        mydb.commit()
                    except Exception as e:
                        print("Unable to display records")
                        print(e)
                def modpsu():
                    import mysql.connector
                    try:
                        mydb=mysql.connector.connect(host='localhost',user='root',passwd="",db='pc_express')
                        mycursor=mydb.cursor()
                        f=input("Enter SQL Command for modifying records:")
                        mycursor.execute(f)
                        print("Records Modified")
                        mydb.commit()
                    except Exception as e:
                        print("Unable to modify record")
                        print(e)
                def delpsu():
                    import mysql.connector
                    try:
                        mydb=mysql.connector.connect(host='localhost',user='root',passwd="",db='pc_express')
                        mycursor=mydb.cursor()
                        b=input("Enter SQL Command to delete records:")
                        mycursor.execute(b)
                        print('Record Deleted')
                        mydb.commit()
                    except Exception as e:
                        print('Unable to delete record')
                        print(e)
                psu()
            if a==7:
                def case():
                    print('1.Add cabinet records')
                    print('2.Update cabinet records')
                    print('3.Display cabinet records')
                    print("4.Modify cabinet records")
                    print('5.Delete cabinet records')
                    print('6.Exit')
                    print('\n')
                    v=int(input("Enter Your Choice"))
                    print("\n")
                    if v==1:
                        addcase()
                    elif v==2:
                        upcase()
                    elif v==3:
                        discase()
                    elif v==4:
                        modcase()
                    elif v==5:
                        delcase()
                    else:
                        ("Returning to main menu...")
                def addcase():
                    import mysql.connector
                    try:
                        mydb=mysql.connector.connect(host='localhost',user='root',passwd="",db='pc_express')
                        mycursor=mydb.cursor()
                        company=input("Enter Company name:")
                        name=input("Enter Product name:")
                        size=input("Enter the Form Factor:")
                        qty=input('Enter Quantity:')
                        price=input('Enter Price:')
                        mycursor.execute("""INSERT INTO cabinet(Company,Name,Form_Factor,Qty,Price)VALUES(%s,%s,%s,%s,%s)""",(company,name,size,qty,price))
                        print('Record Inserted')
                        mydb.commit()
                    except Exception as e:
                        print('Unable to insert record')
                        print(e)
                def upcase():
                    import mysql.connector
                    try:
                        mydb=mysql.connector.connect(host='localhost',user='root',passwd="",db='pc_express')
                        mycursor=mydb.cursor()
                        l=input('Enter the SQL Command for update')
                        mycursor.execute(l)
                        print("Record Updated")
                        mydb.commit()
                    except Exception as e:
                        print("Unable to update record")
                        print(e)
                def discase():
                    import mysql.connector
                    try:
                        mydb=mysql.connector.connect(host='localhost',user='root',passwd="",db='pc_express')
                        mycursor=mydb.cursor()
                        j=input('Enter the SQL Command to display record:')
                        mycursor.execute(j)
                        results=mycursor.fetchall()
                        for s in results:
                            print(s)
                        print('Record Displayed')
                        mydb.commit()
                    except Exception as e:
                        print('Unable to display record')
                        print(e)
                def modcase():
                    import mysql.connector
                    try:
                        mydb=mysql.connector.connect(host='localhost',user='root',passwd="",db='pc_express')
                        mycursor=mydb.cursor()
                        t=input('Enter the SQL Command to modify record:')
                        mycursor.execute(t)
                        print('Record Modified')
                        mydb.commit()
                    except Exception as e:
                        print("Unable to modify record")
                        print(e)
                def delcase():
                    import mysql.connector
                    try:
                        mydb=mysql.connector.connect(host='localhost',user='root',passwd="",db='pc_express')
                        mycursor=mydb.cursor()
                        z=input("Enter the SQL Command to delete record:")
                        mycursor.execute(z)
                        print("Record Deleted")
                        mydb.commit()
                    except Exception as e:
                        print('Unable to delete record')
                        print(e)                    
                case() 
            else:
                print('Returning to main menu...')       


    if choice==2:
        def sale():
            print('1.Add Sales Details records')
            print("2.Update Sales Details records")
            print('3.Display Sales Details records')
            print('4.Modify Sales Details records')
            print('5.Delete Sales Details records')
            print('6.Exit')
            print('\n')
            f=int(input("Enter Your Choice:"))
            print('\n')
            if f==1:
                addsale()
            elif f==2:
                upsale()
            elif f==3:
                dissale()
            elif f==4:
                modsale()
            elif f==5:
                delsale()
            else:
                ('Returing to main menu...')
        def addsale():
            import mysql.connector
            try:
                mydb=mysql.connector.connect(host='localhost',user='root',passwd="",db='pc_express')
                mycursor=mydb.cursor()
                cname=input('Enter Customer name:')
                phno=input('Enter Phone number:')
                dog=input("Enter Description_of_Goods:")
                dop=input('Enter the Date_of_purchase:')
                qty=input('Enter Quantity:')
                price=input('Enter price:')
                mycursor.execute("""INSERT INTO sales_details(C_name,Phone_No,Description_of_Goods,Date_of_purchase,Qty,Price)VALUES(%s,%s,%s,%s,%s,%s)""",(cname,phno,dog,dop,qty,price))
                print('Record Updated')
                mydb.commit()
            except Exception as e:
                print('Unable to insert record')
                print(e)
        def upsale():
            import mysql.connector
            try:
                mydb=mysql.connector.connect(host='localhost',user='root',passwd="",db='pc_express')
                mycursor=mydb.cursor()
                q=input('Enter SQL Command for updating records:')
                mycursor.execute(q)
                print("Record Updates")
                mydb.commit()
            except Exception as e:
                print("Unable to update record")
                print(e)
        def dissale():
            import mysql.connector
            try:
                mydb=mysql.connector.connect(host='localhost',user='root',passwd="",db='pc_express')
                mycursor=mydb.cursor()
                g=input('Enter SQL Command for Displaying records:')
                mycursor.execute(g)
                results=mycursor.fetchall()
                for u in results:
                    print(u)
                print('Record Displayed')
                mydb.commit()
            except Exception as e:
                print("Unable to display record")
                print(e)
        def modsale():
            import mysql.connector
            try:
                mydb=mysql.connector.connect(host='localhost',user='root',passwd="",db='pc_express')
                mycursor=mydb.cursor()
                k=input('Enter SQL Command to modify records:')
                mycursor.execute(k)
                print('Record Modified')
                mydb.commit()
            except Exception as e:
                print('Unable to modify record')
                print(e)
        def delsale():
            import mysql.connector
            try:
                mydb=mysql.connector.connect(host='localhost',user='root',passwd="",db='pc_express')
                mycursor=mydb.cursor()
                i=input('Enter SQL Command to Delete record:')
                mycursor.execute(i)
                print('Record deleted')
                mydb.commit()
            except Exception as e:
                print('Unable to delete Record')
                print(e)
        sale()
    if choice==3:
        exit()

