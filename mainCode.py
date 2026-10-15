import mysql.connector as connector
def mainController():
    while True:
        print("\n")
        print("\t" + "*" * 20)
        print("\tLogin Menu")
        print("\t" + "*" * 20)
        print("\t1.Admin Login\n\t2.User Login\n\t3.Exit")
        print("\t" + "*" * 20)

        ch = int(input("Enter Your Choice: "))

        if ch == 1:
            adminController()
            print("Admin")

        elif ch == 2:
            userController()
            print("User")

        elif ch == 3:
            print("Thank You For Visiting DH Mart.")
            break
        else:
            print("Invalid Choice. Please re-enter.")


def adminController():
    while True:
        print("\n")
        print("\t" + "*" * 20)
        print("\tAdmin Menu")
        print("\t" + "*" * 20)
        print("\t1.Supplier\n\t2.Customer\n\t3.Goods\n\t4.Purchase\n\t5.Reports\n\t6.Back to Main Menu")
        print("\t" + "*" * 20)
        ch = int(input("Enter Your Choice: "))

        if ch == 1:
            supplierController()

        elif ch == 2:
            customerController()

        elif ch == 3:
            goodsController()

        elif ch == 4:
             purchaseController()

        elif ch == 5:
            reportsController()

        elif ch == 6:
            print("Going Back to Main Menu")
            break
        else:
            print("Invalid Choice")

def userController():
    while True:
        print("\n")
        print("\t" + "*" * 20)
        print("\tUser Menu")
        print("\t" + "*" * 20)
        print("\t1.Sales\n\t2.Back to Main Menu")
        print("\t" + "*" * 20)
        ch = int(input("Enter Your Choice: "))

        if ch == 1:
            salesController()

        elif ch == 2:
            print("Going Back to Main Menu")
            break
        else:
            print("Invalid Choice")


def supplierController():
    while True:
        print("\n")
        print("\t" + "*" * 20)
        print("\tSupplier Menu")
        print("\t" + "*" * 20)
        print("\t1.Add New Supplier\n\t2.Edit Existing Supplier\n\t3.Delete Existing Supplier\n\t"
              "4.View all Suppliers\n\t5.Search Supplier ID\n\t6.Search Supplier Name\n\t7.Search Supplier Address\n\t"
              "8.Search Supplier Mobile No\n\t9.Search Goods ID\n\t10.Back to Admin Menu")
        print("\t" + "*" * 20)
        ch = int(input("Enter Your Choice: "))

        if ch == 1:
            addSupplierRecord()

        elif ch == 2:
            editSupplierRecord()

        elif ch == 3:
            deleteSupplierRecord()

        elif ch == 4:
            selectAllSupplierInfo()

        elif ch == 5:
            selectSuppID()

        elif ch == 6:
            selectSuppName()

        elif ch == 7:
            selectSuppAdd()

        elif ch == 8:
            selectSuppMobileNum()

        elif ch == 9:
            selectSuppGoodsID()

        elif ch == 10:
            print("Going back to Admin Menu.")
            break
        else:
            print("Invalid choice")

def customerController():
    while True:
        print("\n")
        print("\t" + "*" * 20)
        print("\tCustomer Menu")
        print("\t" + "*" * 20)
        print("\t1.Add New Customer\n\t2.Edit Existing Customer\n\t3.Delete Existing Customer\n\t"
              "4.View all Customers\n\t5.Search Customer Id\n\t6.Search Customer Name\n\t"
              "7.Search Customer Mobile No\n\t8.Search Customer Age\n\t9.Search Customer Gender\n\t"
              "10.Search Customer DOB\n\t11.Search Customer Address \n\t12.Back to Admin Menu")
        print("\t" + "*" * 20)
        ch = int(input("Enter Your Choice: "))
        if ch == 1:
            addCustomerRecord()

        elif ch == 2:
            editCustomerRecord()

        elif ch == 3:
            deleteCustomerRecord()

        elif ch == 4:
            selectAllCustomerInfo()

        elif ch == 5:
            selectCustomerID()

        elif ch == 6:
            selectCustomerName()

        elif ch == 7:
            selectCustomerMobileNum()

        elif ch == 8:
            selectCustomerAge()

        elif ch == 9:
            selectCustomerGender()

        if ch == 10:
            selectCustomerDateofBirth()

        elif ch == 11:
            selectCustomerAddress()

        elif ch == 12:
            print("Going back to Admin Menu.")
            break
        elif ch not in range(1,13):
            print("Invalid choice.")


def goodsController():
    while True:
        print("\n")
        print("\t" + "*" * 20)
        print("\tGoods Menu")
        print("\t" + "*" * 20)
        print("\t1.Add New Goods\n\t2.Edit Existing Goods\n\t3.Delete Existing Goods\n\t"
              "4.View all Goods\n\t5.Search Goods ID\n\t6.Search Goods Name\n\t7.Search Goods SP\n\t"
              "8.Search Goods Category\n\t9.Search Goods Quantity On Hand\n\t10.Reorder Quantity\n\t"
              "11.Back to Admin Menu")
        print("\t" + "*" * 20)
        ch = int(input("Enter Your Choice: "))
        if ch == 1:
            addGoodsRecord()

        elif ch == 2:
            editGoodsRecord()

        elif ch == 3:
            deleteGoodsRecord()

        elif ch == 4:
            selectAllGoodsInfo()

        elif ch == 5:
            selectGoodsID()

        elif ch == 6:
            selectGoodsName()

        elif ch == 7:
            selectGoodsSellingPrice()

        elif ch == 8:
            selectGoodsCategory()

        elif ch == 9:
            selectGoodsQOH()

        elif ch == 10:
            selectGoodsReorderQuantity()

        elif ch == 11:
            print("Going back to Admin Menu.")
            break
        else:
            print("Invalid choice")

def purchaseController():
    while True:
        print("\n")
        print("\t" + "*" * 20)
        print("\tPurchase Menu")
        print("\t" + "*" * 20)
        print("\t1.Add New Purchase\n\t2.Edit Existing Purchase Record\n\t3.Delete Existing Purchase Record"
              "\n\t4.View all Purchase Record\n\t5.Search Purchase ID\n\t6.Search Purchase Date"
              "\n\t7.Search Quantity Bought\n\t8.Search Purchase Price\n\t9.Back to Admin Menu")
        print("\t" + "*" * 20)
        ch = int(input("Enter Your Choice: "))
        if ch == 1:
            addPurchaseRecord()

        elif ch == 2:
            editPurchaseRecord()

        elif ch == 3:
            deletePurchaseRecord()

        elif ch == 4:
            selectAllPurchaseInfo()

        elif ch == 5:
            selectPurchaseID()

        elif ch == 6:
            selectPurchaseDate()

        elif ch == 7:
            selectPurchaseQTY()

        elif ch == 8:
            selectPurchasePrice()

        elif ch == 9:
            print("Going back to Admin Menu.")
            break
        else:
            print("Invalid choice")

def salesController():
    while True:
        print("\n")
        print("\t" + "*" * 20)
        print("\tSales Menu")
        print("\t" + "*" * 20)
        print("\t1.Add New Sales\n\t2.Edit Existing Sales Record\n\t3.Delete Existing Sales Record"
              "\n\t4.View all Sales Record\n\t5.Search Customer ID\n\t6.Search Goods ID"
              "\n\t7.Search Sales Date\n\t8.Search Quantity Sold\n\t9.Back to Admin Menu")
        print("\t" + "*" * 20)
        ch = int(input("Enter Your Choice: "))
        if ch == 1:
            addSalesRecord()

        elif ch == 2:
            editSalesRecord()

        elif ch == 3:
            deleteSalesRecord()

        elif ch == 4:
            selectAllSalesInfo()

        elif ch == 5:
            selectCustomerIDInSales()

        elif ch == 6:
            selectGoodsIDInSales()

        elif ch == 7:
            selectSalesDate()

        elif ch == 8:
            selectSalesQuantity()

        elif ch == 9:
            print("Going back to Admin Menu.")
            break
        else:
            print("Invalid choice")

def reportsController():
    while True:
        print("\n")
        print("\t" + "*" * 20)
        print("\tReports Menu")
        print("\t" + "*" * 20)
        print("\t1.View all Supplier Record\n\t2.View all Goods Record\n\t3.View all Customer Record"
              "\n\t4.View Daily Sales Details\n\t5.View Monthly Sales Details\n\t6.View Yearly Sales Details"
              "\n\t7.Back to Admin Menu")
        print("\t" + "*" * 20)
        ch = int(input("Enter Your Choice: "))
        if ch == 1:
            selectAllSupplierInfo()

        elif ch == 2:
            selectAllGoodsInfo()

        elif ch == 3:
            selectAllCustomerInfo()

        elif ch == 4:
            displayDailySales()

        elif ch == 5:
            displayMonthlySales()

        elif ch == 6:
            displayYearlySales()

        elif ch == 7:
            print("Going back to Admin Menu.")
            break
        else:
            print("Invalid choice")





#Initialising all supplier parameters.
def inputSupplier():
    def validatedSuppName():
        flag1 = True
        while flag1 is True:
            mySuppName1 = input("Enter Supplier first name: ")
            mySuppName2 = input("Enter Supplier last name: ")
            trimSuppName = mySuppName1 + mySuppName2
            correctedSuppName = mySuppName1 + ' ' + mySuppName2
            if len(trimSuppName) != 0:
                for i in trimSuppName:
                    if not i.isalpha():
                        flag1 = True
                        print('Supplier name can only consist of letters. Please re-enter.')
                        break
                    else:
                        flag1 = False
            else:
                flag1 = True
                print('Supplier name cannot be empty. Please re-enter.')
                continue
            if flag1 is False:
                return correctedSuppName

    sname = validatedSuppName()
    def validatedSuppAddress():
        while True:
            flag = False
            myAdd = input('Enter Supplier Address: ').strip()
            if len(myAdd)>30:
                print('Address too large. Please re-enter.')
                flag = True
            elif len(myAdd)==0:
                print('Address is mandatory. Please re-enter.')
                flag = True

            if flag is False:
                return myAdd
    sadd = validatedSuppAddress()
    def validatedSuppMobile():
        flag = True
        while flag is True:
            myMobile = input('Enter Supplier Mobile Number: ')
            if len(myMobile) == 10:
                for i in myMobile:
                    if not i.isdigit():
                        flag = True
                        print('Enter a valid Mobile number.')
                        break
                    else:
                        flag = False
            elif len(myMobile)==0:
                flag = True
                print ('Supplier Mobile Number is compulsory. Please re-enter.')
            else:
                flag = True
                print('Supplier number can consist only 10 digits. Please re-enter.')
                continue
            if flag is False:
                return myMobile
    smobile = validatedSuppMobile()
    gid = input("Enter Goods ID : ")
    sid=sname[-1]+sadd[-1]+smobile[-1]
    return (sid,sname, sadd, smobile,gid)
#end

#Inputting values for all supplier parameters.
def addSupplierRecord():
    mycon=connector.connect(host='localhost', user='root', password='Eagleseye@512',database='rdbms_project_sem3',
                            auth_plugin='mysql_native_password')
    if not mycon.is_connected:
        print("Error connecting to database.")
    else:
        supplierInfo = inputSupplier()
        myQry="INSERT INTO supplier VALUES(%s,%s,%s,%s,%s)"
        # sid | sname | sadd | smobile | gid |
        myCursor=mycon.cursor()
        myCursor.execute(myQry, supplierInfo)
        mycon.commit()
        print(myCursor.rowcount, "record inserted.")
    mycon.close()
#end - supplier input

#Delete any particular supplier record.
def deleteSupplierRecord():
    mycon = connector.connect(host='localhost', user='root', password='Eagleseye@512', database='rdbms_project_sem3',
                              auth_plugin='mysql_native_password')
    if not mycon.is_connected:
        print("Error connecting to database.")
    else:
        sid = input("Enter the supplier ID to be deleted: ")
        myQry = "DELETE FROM supplier WHERE sid="+"'"+sid+"'"

        myCursor = mycon.cursor()
        myCursor.execute(myQry)
        mycon.commit()

        if myCursor.rowcount:
            print(myCursor.rowcount, "record deleted.")
        else:
            print("Roll Number ",sid, "Does not Exist.")
    mycon.close()
#end - deletion of supplier

#Update any particular supplier record.
def updateSupplierRecord(suppInfo):
    # sid | sname | sadd | smobile | gid |
    sid=suppInfo[0]
    suppInfo = list(suppInfo[1:])
    suppInfo.append(sid)
    # sname | sadd | smobile | gid | sid |

    print("Current Supplier Details ", suppInfo)
    while True:
        print("1. Name\n2.Address\n3.Mobile\n4.Exit")
        ch = int(input("What do you want to edit?"))
        message = ["", "Name ", "Address ", "Mobile"]

        if ch == 4:
            break
        elif ch == 3:
            suppInfo[ch-1] = int(input("Enter Supplier's " + message[ch]))
        else:
            suppInfo[ch-1] = input("Enter Supplier's " + message[ch])

    return tuple(suppInfo)
#end - updating supplier info

#Edit any particular supplier record.
def editSupplierRecord():
    mycon=connector.connect(host='localhost', user='root', password='Eagleseye@512',database='rdbms_project_sem3',
                            auth_plugin='mysql_native_password')
    if not mycon.is_connected:
        print("Error connecting to database:")
    else:
        id=input("Enter supplier ID: ")
        myQry="Select * from supplier where sid="+id
        myCursor=mycon.cursor()

        myCursor.execute(myQry)

        suppInfo=myCursor.fetchone()
        if suppInfo is None:
            print("Supplier ID ",id," does not exist.")
        else:
            suppInfo=updateSupplierRecord(suppInfo)
            print(suppInfo)
            myQry = ("UPDATE supplier set sname=%s,sadd=%s,smobile=%s,gid=%s WHERE sid=%s")
            myCursor.execute(myQry, suppInfo)
            mycon.commit()

            if myCursor.rowcount:
                print(myCursor.rowcount, "record updated.")
        mycon.close()
#end - editing supplier info

#Display all supplier records available.
def selectAllSupplierInfo():
    mycon=connector.connect(host='localhost', user='root', password='Eagleseye@512',database='rdbms_project_sem3',
                            auth_plugin='mysql_native_password')
    if mycon.is_connected == False:
        print("Error connecting to database.")
    else:
        myQry="SELECT * FROM supplier;"

        myCursor = mycon.cursor()
        myCursor.execute(myQry)

        suppInfo = myCursor.fetchall()
        if suppInfo==None:
            print("Supplier Details Not Found")
        else:
            print("     All Supplier Detail:       ")
            print("      SUPPLIER ID      NAME          ADDRESS      MOBILE NO      GOODS ID")
            for oneSupplier in suppInfo:
                print("      "+oneSupplier[0]+"               ",oneSupplier[1],"      ",oneSupplier[2]
                      ,"     ",oneSupplier[3],"   ",oneSupplier[4])
        mycon.close()
#end - supplier info display

#Display any particular supplier ID.
def selectSuppID():
    mycon=connector.connect(host='localhost', user='root', password='Eagleseye@512',database='rdbms_project_sem3',
                            auth_plugin='mysql_native_password')
    if mycon.is_connected == False:
        print("Error connecting to database:")
    else:
        sname = input("Enter supplier's name who's supplier ID has to be searched : ")
        myQry = "SELECT sid FROM supplier WHERE sname='" + sname + "';"

        myCursor = mycon.cursor()
        myCursor.execute(myQry)

        suppInfo = myCursor.fetchone()
        if suppInfo == None:
            print("Customer Details Not Found.")
        else:
            print("     List Of Supplier ID's       ")
            print("     Supplier ID     Supplier Name    ")
            for oneSupplier in suppInfo:
                print("    ", oneSupplier + "             " + sname)
        mycon.close()


#end = supplier ID display

#Display any particular supplier Name.
def selectSuppName():
    mycon=connector.connect(host='localhost', user='root', password='Eagleseye@512',database='rdbms_project_sem3',
                            auth_plugin='mysql_native_password')
    if mycon.is_connected == False:
        print("Error connecting to database:")
    else:
        sid = input("Enter the supplier ID who's name has to be searched: ")
        myQry="SELECT sname FROM supplier WHERE sid='"+sid+"'"

        myCursor = mycon.cursor()
        myCursor.execute(myQry)

        suppInfo = myCursor.fetchone()
        if suppInfo==None:
            print("Supplier Details Not Found.")
        else:
            print("     Supplier Name:       ")
            for oneSupplier in suppInfo:
                print("     ", oneSupplier)
        mycon.close()
#end - supplier name display

#Display any particular supplier address.
def selectSuppAdd():
    mycon=connector.connect(host='localhost', user='root', password='Eagleseye@512',database='rdbms_project_sem3',
                            auth_plugin='mysql_native_password')
    if mycon.is_connected == False:
        print("Error connecting to database.")
    else:
        sid = input("Enter the supplier ID  who's address has to be searched : ")
        myQry="SELECT sadd FROM supplier WHERE sid='"+sid+"'"

        myCursor = mycon.cursor()
        myCursor.execute(myQry)

        suppInfo = myCursor.fetchone()
        if suppInfo==None:
            print("Supplier Details Not Found.")
        else:
            print("     Supplier Address:       ")
            for oneSupplier in suppInfo:
                print("     ", oneSupplier)
        mycon.close()
#end - supplier address display

#Display any particular supplier mobile number.
def selectSuppMobileNum():
    mycon = connector.connect(host='localhost', user='root', password='Eagleseye@512', database='rdbms_project_sem3',
                              auth_plugin='mysql_native_password')
    if mycon.is_connected == False:
        print("Error connecting to database.")
    else:
        sid = input("Enter customer's ID who's mobile number has to be searched: ")
        myQry = "SELECT smobile FROM supplier WHERE sid=" + "sid"

        myCursor = mycon.cursor()
        myCursor.execute(myQry)

        suppInfo = myCursor.fetchone()
        if suppInfo == None:
            print("Supplier Mobile Number Not Found.")
        else:
            print("     Supplier Mobile Number:       ")
            for oneCustomer in suppInfo:
                print("     ", oneCustomer)
        mycon.close()
#end - supplier mobile number display

#Display any particular supplier's goods ID.
def selectSuppGoodsID():
    mycon=connector.connect(host='localhost', user='root', pswd='Eagleseye@512',database='rdbms_project_sem3',
                            auth_plugin="mysql_native_password")
    if mycon.is_connected == False:
        print("Error connecting to database.")
    else:
        sid = input("Enter the supplier ID  who's Goods ID has to be searched : ")
        myQry="SELECT gid FROM supplier WHERE sid="+sid

        myCursor = mycon.cursor()
        myCursor.execute(myQry)

        suppInfo = myCursor.fetchone()
        if suppInfo==None:
            print("Supplier Details Not Found.")
        else:
            print("     Goods ID:       ")
            for oneSupplier in suppInfo:
                print("     ", oneSupplier)
        mycon.close()
#end - supplier goods ID




#Initialising all customer parameters.
def inputCustomer():
    def validatedName():
        flag1 = True
        while flag1 is True:
            myName1 = input("Enter customer's first name: ")
            myName2 = input("Enter customer's last name: ")
            trimName = myName1 + myName2
            correctedName = myName1 + ' ' + myName2
            if len(trimName) != 0:
                for i in trimName:
                    if not i.isalpha():
                        flag1 = True
                        print('Customer name can only consist of letters.')
                        break
                    else:
                        flag1 = False
            else:
                flag1 = True
                print('Customer name cannot be empty.')
                continue
            if flag1 is False:
                return correctedName

    cname = validatedName()
    def validatedAddress():
        while True:
            flag = False
            myAdd = input('Enter Customer Address: ').strip()
            if len(myAdd)>30:
                print('Address too large.')
                flag = True
            elif len(myAdd)==0:
                print('Address is mandatory.')
                flag = True

            if flag is False:
                return myAdd
    cadd = validatedAddress()
    def validatedMobile():
        flag = True
        while flag is True:
            myMobile = input('Enter the Mobile number of Customer: ')
            if len(myMobile) == 10:
                for i in myMobile:
                    if not i.isdigit():
                        flag = True
                        print('Enter a valid Mobile number.')
                        break
                    else:
                        flag = False
            else:
                flag = True
                print('Customer number  can only exist of 10 digits.')
                continue
            if flag is False:
                return myMobile
    cmobile = validatedMobile()

    def validatedGender():
        flag = True
        while flag is True:
            myGen = input("Enter the gender of Customer(F/M): ")
            if len(myGen) == 1:
                if myGen == 'F' or myGen == 'M':
                    flag = False
                else:
                    print('Specify the gender in the form of (M)or (F).')
                    flag = True
            else:
                print('Specify the gender in the form of (M)or (F)')
                flag = True
            if flag is False:
                return myGen
    cgen = validatedGender()

    def validateDate():
        global yy, mm, dd
        flag = True
        while flag is True:
            mydate = input('Enter the date of birth of Customer in the form of DD/MM/YYYY: ')
            datelist = mydate.split("/")
            dd = int(datelist[0])
            mm = int(datelist[1])
            yy = int(datelist[2])
            if 1 <= dd <= 31:
                    if 1 <= mm <= 12:
                        if mm in [4, 6, 9, 11] and dd <= 30:
                            flag = False
                            break
                        elif mm == 2:
                            if yy % 4 == 0 and (yy % 400 == 0 or yy % 100 != 0):
                                if dd > 29:
                                    flag = True
                                    print('Enter Valid date')
                                    continue
                                else:
                                    flag = False
                                    break
                            else:
                                    if dd > 28:
                                        flag = True
                                        print('Enter Valid date.')
                                        continue
                        elif mm in [1, 3, 5, 7, 8, 10, 12] and dd <= 31:
                            flag = False
                        else:
                            flag = True
                            print('Enter Valid date.')
                            continue
                    else:
                        flag = True
                        print('Enter Valid date.')
                        continue
            else:
                    flag = True
                    print('Enter Valid date.')
                    continue
        if flag is False:
            mydate=str(yy)+"/"+str(mm)+"/"+str(dd)
            return mydate

    cdob = validateDate()
    def validateAge():
        flag = True
        while flag is True:
         myAge = input('Enter customer age: ')
         if len(myAge)==2:
            for i in myAge:
              if i.isdigit():
                if 18<=int(myAge)<=80:
                 flag = False
                 break
                else:
                 print('Age of customer must be between 18 and 80.')
                 flag = True
                 break
              else:
                  print('Enter valid age')
                  flag = True

         else:
            print('Enter a valid age where the age of customer is between 18 and 80.')
            flag = True
         if flag is False:
            return myAge
    cage = validateAge()
    cid=cname[-1]+cadd[-1]+cmobile[-1]
    return (cid,cname, cadd, cmobile, cgen, cdob, cage)
#end - customer input

#Inputting values for all customer parameters.
def addCustomerRecord():
    mycon=connector.connect(host='localhost', user='root', password='Eagleseye@512',database='rdbms_project_sem3',
                            auth_plugin='mysql_native_password')
    if (mycon.is_connected == False):
        print("Error connecting to database")
    else:
        customerInfo = inputCustomer()
        myQry="INSERT INTO customer VALUES(%s,%s,%s,%s,%s,%s,%s)"
        # cid | cname | cadd | cmobile | cgen | cdob | cage
        myCursor=mycon.cursor()
        myCursor.execute(myQry, customerInfo)
        mycon.commit()
        print(myCursor.rowcount, "record inserted.")
    mycon.close()

def updateCustomerRecord(cusInfo):
    # cid | cname | cadd | cmobile | cage |
    cid=cusInfo[0]
    cusInfo = list(cusInfo[1:])
    cusInfo.append(cid)
    # cname | cadd | cmobile | cage | cid |

    print("Current Customer Details ", cusInfo)
    while True:
        print("1.Name\n2.Address\n3.Mobile\n4.Age\n5.Exit ")
        ch = int(input("What do you want to edit "))
        message = ["", "Name ", "Address ", "Mobile","Age"]

        if ch == 5:
            break
        elif ch == 4:
            cusInfo[ch-1] = int(input("Enter Customer's " + message[ch]))
        else:
            cusInfo[ch-1] = input("Enter Customer's " + message[ch])
    return tuple(cusInfo)

def editCustomerRecord():
    mycon=connector.connect(host='localhost', user='root', password='Eagleseye@512',database='rdbms_project_sem3',
                            auth_plugin='mysql_native_password')
    if mycon.is_connected == False:
        print("Error connecting to database.")
    else:
        cid=input("Enter customer ID : ")
        myQry="Select * from customer where cid="+cid
        myCursor=mycon.cursor()

        myCursor.execute(myQry)

        cusInfo=myCursor.fetchone()
        if cusInfo==None:
            print("Customer ID ",cid," does not exist.")
        else:
            cusInfo=updateCustomerRecord(cusInfo)
            print(cusInfo)
            myQry = ("UPDATE customer set cname=%s,cadd=%s,cmobile=%s, cgen=%s, cdob=%s, "
                     "cage=%s WHERE cid=%s")
            myCursor.execute(myQry, cusInfo)
            mycon.commit()

            if myCursor.rowcount:
                print(myCursor.rowcount, "record updated.")
        mycon.close()

def deleteCustomerRecord():
    mycon = connector.connect(host='localhost', user='root', password='Eagleseye@512', database='rdbms_project_sem3',
                              auth_plugin='mysql_native_password')
    if (mycon.is_connected == False):
        print("Error connecting to database.")
    else:
        cid = input("Enter the customer ID to be deleted: ")
        myQry = "DELETE FROM customer WHERE cid="+"cid"

        myCursor = mycon.cursor()
        myCursor.execute(myQry)
        mycon.commit()

        if myCursor.rowcount:
            print(myCursor.rowcount, "record deleted.")
        else:
            print("Customer ID ",cid, " Does not Exist.")
    mycon.close()

def selectAllCustomerInfo():
    mycon=connector.connect(host='localhost', user='root', password='Eagleseye@512',database='rdbms_project_sem3',
                            auth_plugin='mysql_native_password')
    if not mycon.is_connected:
        print("Error connecting to database:")
    else:
        myQry="SELECT * FROM customer;"

        myCursor = mycon.cursor()
        myCursor.execute(myQry)

        cusInfo = myCursor.fetchall()
        if cusInfo==None:
            print("Customer Details Not Found")
        else:
            print("     All Customer Detail:       ")
            print("      CUSTOMER ID      NAME                    ADDRESS      MOBILE NO      GENDER     DOB"
                  "              AGE")
            for oneCustomer in cusInfo:
                print("     " , oneCustomer[0] , "            ", oneCustomer[1], "         ",
                      oneCustomer[2], "      ", oneCustomer[3], "   ", oneCustomer[4],"        ",
                      oneCustomer[5],"     " ,oneCustomer[6])
        mycon.close()



def selectCustomerID():
    mycon=connector.connect(host='localhost', user='root', password='Eagleseye@512',database='rdbms_project_sem3',
                            auth_plugin='mysql_native_password')
    if mycon.is_connected == False:
        print("Error connecting to database:")
    else:
        cname = input("Enter customer's name who's customer ID has to be searched : ")
        myQry="SELECT cid FROM customer WHERE cname="+"'"+cname+"'"+";"

        myCursor = mycon.cursor()
        myCursor.execute(myQry)

        cusInfo=myCursor.fetchone()
        if cusInfo==None:
            print("Customer Details Not Found.")
        else:
            print("     List Of Customer ID's       ")
            print("     Customer ID     Customer Name    ")
            for oneCustomer in cusInfo:
                print("    ", oneCustomer+"             "+cname)
        mycon.close()

def selectCustomerName():
    mycon=connector.connect(host='localhost', user='root', password='Eagleseye@512',database='rdbms_project_sem3',
                            auth_plugin='mysql_native_password')
    if mycon.is_connected == False:
        print("Error connecting to database.")
    else:
        cid = input("Enter customer's ID who's customer name has to be searched: ")
        myQry="SELECT cname FROM customer WHERE cid="+"cid"

        myCursor = mycon.cursor()
        myCursor.execute(myQry)

        cusInfo = myCursor.fetchone()
        if cusInfo==None:
            print("Customer Details Not Found.")
        else:
            print("     Customer Name:       ")
            for oneCustomer in cusInfo:
                print("     ",oneCustomer)
        mycon.close()

def selectCustomerMobileNum():
    mycon=connector.connect(host='localhost', user='root', password='Eagleseye@512',database='rdbms_project_sem3',
                            auth_plugin='mysql_native_password')
    if mycon.is_connected == False:
        print("Error connecting to database.")
    else:
        cid = input("Enter customer's ID who's mobile number has to be searched: ")
        myQry="SELECT cmobile FROM customer WHERE cid="+"cid"

        myCursor = mycon.cursor()
        myCursor.execute(myQry)

        cusInfo = myCursor.fetchone()
        if cusInfo==None:
            print("Customer Mobile Number Not Found.")
        else:
            print("     Customer Mobile Number:       ")
            for oneCustomer in cusInfo:
                print("     ", oneCustomer)
        mycon.close()

def selectCustomerAge():
    mycon=connector.connect(host='localhost', user='root', password='Eagleseye@512',database='rdbms_project_sem3',
                            auth_plugin='mysql_native_password')
    if mycon.is_connected == False:
        print("Error connecting to database.")
    else:
        cid=input("Enter customer's ID who's age has to be searched: ")
        myQry="SELECT cage FROM customer WHERE cid="+"cid"

        myCursor = mycon.cursor()
        myCursor.execute(myQry)

        cusInfo = myCursor.fetchone()
        if cusInfo==None:
            print("Customer Age Not Found.")
        else:
            print("     Customer Age:       ")
            for oneCustomer in cusInfo:
                print("     ", oneCustomer)
        mycon.close()

def selectCustomerGender():
    mycon=connector.connect(host='localhost', user='root', password='Eagleseye@512',database='rdbms_project_sem3',
                            auth_plugin='mysql_native_password')
    if mycon.is_connected == False:
        print("Error connecting to database.")
    else:
        cid=input("Enter customer's ID who's gender has to be searched: ")
        myQry="SELECT cgen FROM customer WHERE cid="+"cid"

        myCursor = mycon.cursor()
        myCursor.execute(myQry)

        cusInfo = myCursor.fetchone()
        if cusInfo==None:
            print("Customer Gender Not Found.")
        else:
            print("     Customer Gender:       ")
            for oneCustomer in cusInfo:
                print("     ", oneCustomer)
        mycon.close()

def selectCustomerDateofBirth():
    mycon=connector.connect(host='localhost', user='root', password='Eagleseye@512',database='rdbms_project_sem3',
                            auth_plugin='mysql_native_password')
    if mycon.is_connected == False:
        print("Error connecting to database.")
    else:
        cid=input("Enter customer's ID who's date of birth has to be searched: ")
        myQry="SELECT cdob FROM customer WHERE cid="+"cid"

        myCursor = mycon.cursor()
        myCursor.execute(myQry)

        cusInfo = myCursor.fetchone()
        if cusInfo==None:
            print("Customer Date Of Birth Not Found.")
        else:
            print("     Customer Date Of Birth:       ")
            for oneCustomer in cusInfo:
                print("     ", oneCustomer)
        mycon.close()

def selectCustomerAddress():
    mycon=connector.connect(host='localhost', user='root', password='Eagleseye@512',database='rdbms_project_sem3',
                            auth_plugin='mysql_native_password')
    if mycon.is_connected == False:
        print("Error connecting to database.")
    else:
        cid=input("Enter customer's ID who's address has to be searched: ")
        myQry="SELECT cadd FROM customer WHERE cid="+"cid"

        myCursor = mycon.cursor()
        myCursor.execute(myQry)

        cusInfo = myCursor.fetchone()
        if cusInfo==None:
            print("Customer Address Not Found.")
        else:
            print("     Customer Address:       ")
            for oneCustomer in cusInfo:
                print("     ", oneCustomer)
        mycon.close()





#Initialising all goods parameters.
def inputGoods():

    def validatedGName():
        flag1 = True
        while flag1 is True:
            myGName1 = input("Enter Goods name: ")
            if len(myGName1) != 0:
                for i in myGName1:
                    if not i.isalpha():
                        flag1 = True
                        print('Goods name can only consist of letters.')
                        break
                    else:
                        flag1 = False
            else:
                flag1 = True
                print('Goods name cannot be empty.')
                continue
            if flag1 is False:
                return myGName1
    gname = validatedGName()
    gid = input("Enter Goods ID")

    def validatedSprice():
        flag1=True
        while flag1 is True:
            mySprice1 =int(input("Enter Goods Selling Price: "))
            strprice= str(mySprice1)
            if len(strprice) != 0:
                for i in strprice:
                    if not i.isdigit():
                        flag1=True
                        print ("Goods Price can only contain Digits.")
                        break
                    elif int(strprice) > 7000:
                        flag1=True
                        print ("Max Price is Rs. 7000.")
                        break
                    else:
                        flag1=False
            else:
                flag1=True
                print("Goods must have a price.")
                continue
            if flag1 is False:
                return mySprice1

    sprice = validatedSprice()

    def validatedGqoh():
        flag1 = True
        while flag1 is True:
            myGqoh = int(input("Enter no. of Goods currently in stock: "))
            strqoh= str(myGqoh)
            if len(strqoh) != 0:
                for i in strqoh:
                    if not i.isdigit():
                        flag1 = True
                        print('Quantity of hand can only be a number.')
                        break
                    elif myGqoh<15:
                        flag1 = True
                        print('Quantity needs a restock.')
                    else:
                        flag1 = True
            else:
                flag1 = True
                print('Number of goods cannot be 0, RESTOCK IMMEDIATELY.')
                continue
            if flag1 is False:
                return myGqoh

    gqoh = validatedGqoh()


    def validatedGorder():
        flag1 = True
        while flag1 is True:
            myGoid = int(input("Enter Goods Order number: "))
            sGoid=str(myGoid)
            if len(sGoid) != 0:
                for i in sGoid:
                    if not i.isdigit():
                        flag1 = True
                        print('Goods re-order quantity can only consist of numbers.')
                        break
                    else:
                        flag1 = False
            else:
                flag1 = True
                print('Goods re-order quantity cannot be empty.')
                continue
            if flag1 is False:
                return myGoid

    greorder = validatedGorder()


    def validatedGcat():
        flag1 = True
        while flag1 is True:
            myGcat = input("Enter Goods category: ")
            if len(myGcat) != 0:
                for i in myGcat:
                    if not i.isalpha():
                        flag1 = True
                        print('Goods category can only consist of letters.')
                        break
                    else:
                        flag1 = False
            else:
                flag1 = True
                print('Goods must have a category.')
                continue
            if flag1 is False:
                return myGcat

    gcat = validatedGcat()

    gexp = input("Enter Goods Expiry Date")
    return(gid, gname, sprice, gqoh, greorder, gcat, gexp)

#Inputting values for all goods parameters.
def addGoodsRecord():
    mycon=connector.connect(host='localhost', user='root', password='Eagleseye@512',database='rdbms_project_sem3',
                            auth_plugin='mysql_native_password')
    if (mycon.is_connected == False):
        print("Error connecting to database:")
    else:
        goodsInfo = inputGoods()
        myQry="INSERT INTO goods VALUES(%s,%s,%s,%s,%s,%s,%s)"
        # gid | gname | sprice | gqoh | greorder | gcat | gexp
        myCursor=mycon.cursor()
        myCursor.execute(myQry, goodsInfo)
        mycon.commit()
        print(myCursor.rowcount, "record inserted.")
    mycon.close()

def updateGoodsRecord(goodsInfo):
    # gid | gname | sprice | gqoh | greorder | gcat | gexp
    gid=goodsInfo[0]
    goodsInfo = list(goodsInfo[1:])
    goodsInfo.append(gid)
    # gname | sprice | gqoh | greorder | gcat | gexp | gid

    print("Current Goods Details", goodsInfo)
    while True:
        print("1.Name\n2.Price\n3.Quantity On Hand\n4.Reorder Quantity\n5.Category\n6.Expiry Date\n7.Exit ")
        ch = int(input("What do you want to edit: "))
        message = ["", "Name ", "Price ", "Quantity On Hand","Reorder Quantity","Category","Expiry Date"]

        if ch == 7:
            break
        elif ch == 6:
            goodsInfo[ch-1] = int(input("Enter Goods's " + message[ch]))
        else:
            goodsInfo[ch-1] = input("Enter Goods's " + message[ch])
    return tuple(goodsInfo)

def editGoodsRecord():
    mycon=connector.connect(host='localhost', user='root', password='Eagleseye@512',database='rdbms_project_sem3',
                            auth_plugin='mysql_native_password')
    if mycon.is_connected == False:
        print("Error connecting to database.")
    else:
        gid=input("Enter Goods ID which needs to be edited: ")
        myQry="SELECT * FROM goods WHERE gid='"+gid+"'"
        myCursor=mycon.cursor()

        myCursor.execute(myQry)

        goodsInfo=myCursor.fetchone()
        if goodsInfo==None:
            print("Goods ID",gid,"does not exist.")
        else:
            goodsInfo=updateGoodsRecord(goodsInfo)
            print(goodsInfo)
            myQry = ("UPDATE goods SET gname=%s,sprice=%s,gqoh=%s, greorder=%s, gcat=%s,gexp=%s WHERE gid=%s")
            myCursor.execute(myQry, goodsInfo)
            mycon.commit()

            if myCursor.rowcount:
                print(myCursor.rowcount, "record updated")
        mycon.close()

def selectAllGoodsInfo():
    mycon=connector.connect(host='localhost', user='root', password='Eagleseye@512',database='rdbms_project_sem3',
                            auth_plugin='mysql_native_password')
    if mycon.is_connected == False:
        print("Error connecting to database.")
    else:
        myQry="SELECT * FROM goods;"

        myCursor = mycon.cursor()
        myCursor.execute(myQry)

        goodsInfo = myCursor.fetchall()
        if goodsInfo==None:
            print("Goods Details Not Found.")
        else:
            print("     All Goods Detail:       ")
            print("     GOODS ID     GNAME         SELLING PRICE     QOH     REORDER QTY"
                  "     GOODS CATEGORY       EXPIRY DATE")
            for oneGoods in goodsInfo:
                print("     ", oneGoods[0],"         ", oneGoods[1],"        ", oneGoods[2],
                      "           ", oneGoods[3],"   ", oneGoods[4],"           ", oneGoods[5],
                      "         ",oneGoods[6])
        mycon.close()

def deleteGoodsRecord():
    mycon = connector.connect(host='localhost', user='root', password='Eagleseye@512', database='rdbms_project_sem3',
                              auth_plugin='mysql_native_password')
    if not mycon.is_connected:
        print("Error connecting to database.")
    else:
        gid = input("Enter the Goods ID to be deleted: ")
        myQry = "DELETE FROM goods WHERE gid="+gid

        myCursor = mycon.cursor()
        myCursor.execute(myQry)
        mycon.commit()

        if myCursor.rowcount:
            print(myCursor.rowcount, "record deleted.")
        else:
            print("Goods ID ",gid, " Does not Exist")
    mycon.close()

def selectGoodsID():
    mycon=connector.connect(host='localhost', user='root', password='Eagleseye@512',database='rdbms_project_sem3',
                            auth_plugin='mysql_native_password')
    if not mycon.is_connected:
        print("Error connecting to database.")
    else:
        gname = input("Enter Goods' name who's Goods ID has to be searched: ")
        myQry="SELECT gid FROM goods WHERE gname="+"'"+gname+"'"+";"

        myCursor = mycon.cursor()
        myCursor.execute(myQry)

        goodsInfo=myCursor.fetchone()
        if goodsInfo==None:
            print("Goods Details Not Found.")
        else:
            print("Goods ID of",gname,"is: ", end="")
            """print("Goods ID     Goods Name    ")"""
            for oneGoods in goodsInfo:
                print(oneGoods)
        mycon.close()

def selectGoodsName():
    mycon=connector.connect(host='localhost', user='root', password='Eagleseye@512',database='rdbms_project_sem3',
                            auth_plugin='mysql_native_password')
    if not mycon.is_connected:
        print("Error connecting to database.")
    else:
        gid = input("Enter Goods's ID who's Goods name has to be searched: ")
        myQry="SELECT gname FROM goods WHERE gid="+gid+";"

        myCursor = mycon.cursor()
        myCursor.execute(myQry)

        goodsInfo = myCursor.fetchone()
        if goodsInfo==None:
            print("Goods Details Not Found.")
        else:
            print("     Goods Name:       ")
            for oneGoods in goodsInfo:
                print("     ",oneGoods)
        mycon.close()

def selectGoodsSellingPrice():
    mycon=connector.connect(host='localhost', user='root', password='Eagleseye@512',database='rdbms_project_sem3',
                            auth_plugin='mysql_native_password')
    if not mycon.is_connected:
        print("Error connecting to database.")
    else:
        gid = input("Enter Goods's ID who's Selling Price has to be searched: ")
        myQry="SELECT sprice FROM goods WHERE gid="+gid+";"

        myCursor = mycon.cursor()
        myCursor.execute(myQry)

        goodsInfo = myCursor.fetchone()
        if goodsInfo==None:
            print("Goods Details Not Found.")
        else:
            print("     Selling Price of Goods:       ")
            for oneGoods in goodsInfo:
                print("     ",oneGoods)
        mycon.close()

def selectGoodsCategory():
    mycon=connector.connect(host='localhost', user='root', password='Eagleseye@512',database='rdbms_project_sem3',
                            auth_plugin='mysql_native_password')
    if not mycon.is_connected:
        print("Error connecting to database:")
    else:
        gid = input("Enter Goods's ID who's Category has to be searched : ")
        myQry="SELECT gcat FROM goods WHERE gid="+gid+";"

        myCursor = mycon.cursor()
        myCursor.execute(myQry)

        goodsInfo = myCursor.fetchone()
        if goodsInfo==None:
            print("Goods Details Not Found")
        else:
            print("     Category of Goods:       ")
            for oneGoods in goodsInfo:
                print("     ",oneGoods)
        mycon.close()

def selectGoodsQOH():
    mycon=connector.connect(host='localhost', user='root', password='Eagleseye@512',database='rdbms_project_sem3',
                            auth_plugin='mysql_native_password')
    if not mycon.is_connected:
        print("Error connecting to database:")
    else:
        gid = input("Enter Goods's ID who's Quantity On Hand has to be searched : ")
        myQry="SELECT gqoh FROM goods WHERE gid="+gid+";"

        myCursor = mycon.cursor()
        myCursor.execute(myQry)

        goodsInfo = myCursor.fetchone()
        if goodsInfo==None:
            print("Goods Details Not Found")
        else:
            print("     QOH of Goods:       ")
            for oneGoods in goodsInfo:
                print("     ",oneGoods)
        mycon.close()

def selectGoodsReorderQuantity():
    mycon=connector.connect(host='localhost', user='root', password='Eagleseye@512',database='rdbms_project_sem3',
                            auth_plugin='mysql_native_password')
    if not mycon.is_connected:
        print("Error connecting to database:")
    else:
        gid = input("Enter Goods's ID who's Reorder Quantity has to be searched : ")
        myQry="SELECT greorder FROM goods WHERE gid="+gid+";"

        myCursor = mycon.cursor()
        myCursor.execute(myQry)

        goodsInfo = myCursor.fetchone()
        if goodsInfo==None:
            print("Goods Details Not Found")
        else:
            print("     Reorder Quantity of Goods:       ")
            for oneGoods in goodsInfo:
                print("     ",oneGoods)
        mycon.close()




def inputPurchase():
    sid = input("Enter Supplier ID : ")
    if validateSuppID(sid)==False:
        print("Supplier details not found")
    else:
        gid = input("Enter Goods ID : ")
        if validateGoodsID(gid) == False:
            print("Goods details not found")
        else:
            pid = generatePurchaseID()
            pdate = input("Enter Purchase Date : ")
            pqty = int(input("Enter Purchase Quantity : "))
            pprice = float(input("Enter Purchase Price : "))
            return(pid, pdate, pqty, sid, gid, pprice)



def validateSuppID(supid):
    mycon=connector.connect(host='localhost', user='root', password='Eagleseye@512',database='rdbms_project_sem3',
                            auth_plugin='mysql_native_password')
    if mycon.is_connected == False:
        print("Error connecting to database.")
    else:
        myQry="SELECT sid FROM supplier where sid="+"'"+supid+"'"
        myCursor = mycon.cursor()
        myCursor.execute(myQry)
        supInfo=myCursor.fetchone()
        mycon.close()
        if supInfo==None:
            return False
        else:
            return True

def validateGoodsID(goodsid):
    mycon = connector.connect(host='localhost', user='root', password='Eagleseye@512', database='rdbms_project_sem3',
                              auth_plugin='mysql_native_password')
    if not mycon.is_connected:
        print("Error connecting to database:")
    else:
        myQry = "SELECT gid FROM Goods where gid=" + goodsid
        myCursor = mycon.cursor()
        myCursor.execute(myQry)
        goodsInfo = myCursor.fetchone()
        mycon.close()
        if goodsInfo == None:
            return False
        else:
            return True

def generatePurchaseID():
    mycon = connector.connect(host='localhost', user='root', password='Eagleseye@512', database='rdbms_project_sem3',
                              auth_plugin='mysql_native_password')
    if not mycon.is_connected:
        print("Error connecting to database:")
    else:
        myQry = "SELECT pid FROM Purchase Order by pid desc"
        myCursor = mycon.cursor()
        myCursor.execute(myQry)
        pInfo = myCursor.fetchone()
        mycon.close()
        if pInfo == None:
            return 1
        else:
            return int(pInfo[0])+1

def addPurchaseRecord():
    mycon=connector.connect(host='localhost', user='root', password='Eagleseye@512',database='rdbms_project_sem3',
                            auth_plugin='mysql_native_password')
    if not mycon.is_connected:
        print("Error connecting to database:")
    else:
        purchaseInfo = inputPurchase()
        myQry="INSERT INTO purchase VALUES(%s,%s,%s,%s,%s,%s)"
        # pid | pdate | pqty | sid | gid | pprice
        myCursor=mycon.cursor()
        myCursor.execute(myQry, purchaseInfo)
        mycon.commit()
        print(myCursor.rowcount, "record inserted.")
    mycon.close()

def updatePurchaseRecord(purchaseInfo):
    # pid | pdate | pqty | sid | gid | pprice
    pid=purchaseInfo[0]
    purchaseInfo = list(purchaseInfo[1:])
    purchaseInfo.append(pid)
    # pdate | pqty | sid | gid | pprice | pid

    print("Current Purchase Details ", purchaseInfo)
    while True:
        print("1.Date\n2.Quantity\n3.Supplier ID\n4.Goods ID\n5.Purchase Price\n6.Exit")
        ch = int(input("What do you want to edit  : "))
        message = ["", "Date", "Quantity", "Supplier ID","Goods ID","Purchase Price"]

        if ch == 6:
            break
        elif ch == 5:
            purchaseInfo[ch-1] = int(input("Enter Purchase " + message[ch]))
        else:
            purchaseInfo[ch-1] = input("Enter Purchase " + message[ch])
    return tuple(purchaseInfo)

def editPurchaseRecord():
    mycon=connector.connect(host='localhost', user='root', password='Eagleseye@512',database='rdbms_project_sem3',
                            auth_plugin='mysql_native_password')
    if not mycon.is_connected:
        print("Error connecting to database:")
    else:
        pid=input("Enter purchase ID : ")
        myQry="Select * FROM purchase WHERE pid="+pid
        myCursor=mycon.cursor()

        myCursor.execute(myQry)

        purchaseInfo=myCursor.fetchone()
        if purchaseInfo==None:
            print("Customer ID ",pid," does not exist.")
        else:
            purchaseInfo=updatePurchaseRecord(purchaseInfo)
            print(purchaseInfo)
            myQry = "UPDATE purchase set pdate=%s,pqty=%s,sid=%s, gid=%s, pprice=%s WHERE pid=%s"
            myCursor.execute(myQry, purchaseInfo)
            mycon.commit()

            if myCursor.rowcount:
                print(myCursor.rowcount, "record updated")
        mycon.close()

def deletePurchaseRecord():
    mycon = connector.connect(host='localhost', user='root', password='Eagleseye@512', database='rdbms_project_sem3',
                              auth_plugin='mysql_native_password')
    if not mycon.is_connected:
        print("Error connecting to database:")
    else:
        pid = input("Enter the purchase ID to be deleted : ")
        myQry = "DELETE FROM purchase WHERE pid="+pid

        myCursor = mycon.cursor()
        myCursor.execute(myQry)
        mycon.commit()

        if myCursor.rowcount:
            print(myCursor.rowcount, "record deleted.")
        else:
            print("Purchase ID ",pid, "Does not Exist")
    mycon.close()

def selectAllPurchaseInfo():
    mycon=connector.connect(host='localhost', user='root', password='Eagleseye@512',database='rdbms_project_sem3',
                            auth_plugin='mysql_native_password')
    if not mycon.is_connected:
        print("Error connecting to database:")
    else:
        myQry="SELECT * FROM purchase;"

        myCursor = mycon.cursor()
        myCursor.execute(myQry)

        purchaseInfo = myCursor.fetchall()
        if purchaseInfo==None:
            print("Purchase Details Not Found")

        else:
            print("     All Purchase Detail:       ")
            print("      PID      PDATE             PURCHASE QTY     SID        GID         PPRICE")
            for onePurchase in purchaseInfo:
                print("     ", onePurchase[0], "      ", onePurchase[1], "      ", onePurchase[2],
                      "              ", onePurchase[3], "      ", onePurchase[4], "         ", onePurchase[5])
        mycon.close()


def selectPurchaseID():
    mycon=connector.connect(host='localhost', user='root', password='Eagleseye@512',database='rdbms_project_sem3',
                            auth_plugin='mysql_native_password')
    if not mycon.is_connected:
        print("Error connecting to database:")
    else:
        sid=input("Enter supplier ID to search the PID: ")
        myQry="SELECT pid FROM purchase WHERE sid='"+sid+"'"

        myCursor = mycon.cursor()
        myCursor.execute(myQry)

        purchaseInfo=myCursor.fetchone()
        if purchaseInfo==None:
            print("Goods Details Not Found")
        else:
            print("     Purchase ID     ")
            for onePurchase in purchaseInfo:
                print("     ", onePurchase)
        mycon.close()

def selectPurchaseDate():
    mycon=connector.connect(host='localhost', user='root', password='Eagleseye@512',database='rdbms_project_sem3',
                            auth_plugin='mysql_native_password')
    if not mycon.is_connected:
        print("Error connecting to database:")
    else:
        pid = input("Enter PID to search purchase date: ")
        myQry="SELECT pdate FROM purchase WHERE pid='"+pid+"'"

        myCursor = mycon.cursor()
        myCursor.execute(myQry)

        purchaseInfo=myCursor.fetchone()
        if purchaseInfo==None:
            print("Goods Details Not Found")
        else:
            print("     Purchase Date     ")
            for onePurchase in purchaseInfo:
                print("     ", onePurchase)
        mycon.close()

def selectPurchaseQTY():
    mycon=connector.connect(host='localhost', user='root', password='Eagleseye@512',database='rdbms_project_sem3',
                            auth_plugin='mysql_native_password')
    if not mycon.is_connected:
        print("Error connecting to database:")
    else:
        pid = input("Enter PID to search purchase quantity: ")
        myQry="SELECT pqty FROM purchase WHERE pid='"+pid+"'"

        myCursor = mycon.cursor()
        myCursor.execute(myQry)

        purchaseInfo=myCursor.fetchone()
        if purchaseInfo==None:
            print("Purchase Quantity Not Found")
        else:
            print("     Purchase Quantity     ")
            for onePurchase in purchaseInfo:
                print("     ", onePurchase)
        mycon.close()

def selectPurchasePrice():
    mycon=connector.connect(host='localhost', user='root', password='Eagleseye@512',database='rdbms_project_sem3',
                            auth_plugin='mysql_native_password')
    if not mycon.is_connected:
        print("Error connecting to database.")
    else:
        pid=input("Enter PID to search purchase price: ")
        myQry="SELECT pprice FROM purchase WHERE pid='"+pid+"'"

        myCursor = mycon.cursor()
        myCursor.execute(myQry)

        purchaseInfo=myCursor.fetchone()
        if purchaseInfo==None:
            print("Goods Details Not Found")
        else:
            print("     Purchase Price    ")
            for onePurchase in purchaseInfo:
                print("     ", onePurchase)
        mycon.close()






#Initialising all sales parameters.
def inputSales():
    cid = input("Enter Customer ID: ")
    if not validateCustomerIDforSales(cid):
        print("Customer details not found")
    else:
        gid = input("Enter Goods ID: ")
        if not validateGoodsIDforSales(gid):
            print("Goods details not found")
        else:
            salesid = generateSalesID()
            salesdate = input("Enter Sales Date: ")
            salesqty = int(input("Enter Sales Quantity: "))
            return(salesid, cid, gid, salesdate, salesqty)

def generateSalesID():
    mycon = connector.connect(host='localhost', user='root', password='Eagleseye@512', database='rdbms_project_sem3',
                              auth_plugin='mysql_native_password')
    if mycon.is_connected == False:
        print("Error connecting to database:")
    else:
        myQry = "SELECT salesid FROM sales Order by salesid desc"
        myCursor = mycon.cursor()
        myCursor.execute(myQry)
        salesInfo = myCursor.fetchone()
        mycon.close()
        if salesInfo == None:
            return 1
        else:
            return int(salesInfo[0])+1

def addSalesRecord():
    mycon=connector.connect(host='localhost', user='root', password='Eagleseye@512',database='rdbms_project_sem3',
                            auth_plugin='mysql_native_password')
    if (mycon.is_connected == False):
        print("Error connecting to database:")
    else:
        salesInfo = inputSales()
        myQry="INSERT INTO sales VALUES(%s,%s,%s,%s,%s)"
        # salesid | cid | gid | salesdate | salesqty |
        myCursor=mycon.cursor()
        myCursor.execute(myQry, salesInfo)
        mycon.commit()
        print(myCursor.rowcount, "record inserted.")
    mycon.close()

def validateCustomerIDforSales(cusid):
    mycon=connector.connect(host='localhost', user='root', password='Eagleseye@512',database='rdbms_project_sem3',
                            auth_plugin='mysql_native_password')
    if mycon.is_connected == False:
        print("Error connecting to database:")
    else:
        myQry="SELECT cid FROM customer WHERE cid="+"'"+cusid+"'"
        myCursor = mycon.cursor()
        myCursor.execute(myQry)
        supInfo=myCursor.fetchone()
        mycon.close()
        if supInfo==None:
            return False
        else:
            return True

def validateGoodsIDforSales(goodsid):
    mycon = connector.connect(host='localhost', user='root', password='Eagleseye@512', database='rdbms_project_sem3',
                              auth_plugin='mysql_native_password')
    if mycon.is_connected == False:
        print("Error connecting to database:")
    else:
        myQry = "SELECT gid FROM goods where gid=" + goodsid+";"
        myCursor = mycon.cursor()
        myCursor.execute(myQry)
        goodsInfo = myCursor.fetchone()
        mycon.close()
        if goodsInfo == None:
            return False
        else:
            return True

def updateSalesRecord(salesInfo):
    # salesid | cid | gid | salesdate | salesqty |
    sid=salesInfo[0]
    salesInfo = list(salesInfo[1:])
    salesInfo.append(sid)
    # salesdate | salesqty | salesid | cid | gid |

    print("Current Sales Details ", salesInfo)
    while True:
        print("1. Sales Date\n2. Sales Quantity\n3. Exit")
        ch = int(input("What do you want to edit: "))
        message = ["","","", " Sales Date", "Sales Quantity"]

        if ch == 3:
            break
        elif ch == 2:
            salesInfo[ch+2] = int(input("Enter New sales quantity : " + message[ch]))
        else:
            salesInfo[ch+2] = input("Enter new sales date : " + message[ch])
    return tuple(salesInfo)

def editSalesRecord():
    mycon=connector.connect(host='localhost', user='root', password='Eagleseye@512',database='rdbms_project_sem3',
                            auth_plugin='mysql_native_password')
    if mycon.is_connected == False:
        print("Error connecting to database:")
    else:
        sid=input("Enter Sales ID which needs to be edited: ")
        myQry="Select * FROM sales WHERE salesid="+sid
        myCursor=mycon.cursor()

        myCursor.execute(myQry)

        salesInfo=myCursor.fetchone()
        if salesInfo==None:
            print("Sales ID ",sid," does not exist.")
        else:
            salesInfo=updateSalesRecord(salesInfo)
            print(salesInfo)
            myQry = ("UPDATE sales SET salesdate=%s,salesqty=%s WHERE sid=%s")
            myCursor.execute(myQry, salesInfo)
            mycon.commit()

            if myCursor.rowcount:
                print(myCursor.rowcount, "record updated")
        mycon.close()

def deleteSalesRecord():
    mycon = connector.connect(host='localhost', user='root', password='Eagleseye@512', database='rdbms_project_sem3',
                              auth_plugin='mysql_native_password')
    if not mycon.is_connected:
        print("Error connecting to database:")
    else:
        sid = input("Enter the sales ID to be deleted: ")
        myQry = "DELETE FROM sales WHERE salesid="+sid

        myCursor = mycon.cursor()
        myCursor.execute(myQry)
        mycon.commit()

        if myCursor.rowcount:
            print(myCursor.rowcount, "record deleted.")
        else:
            print("Sales ID",sid,"Does not Exist")
    mycon.close()

def selectAllSalesInfo():
    mycon=connector.connect(host='localhost', user='root', password='Eagleseye@512',database='rdbms_project_sem3',
                            auth_plugin='mysql_native_password')
    if mycon.is_connected == False:
        print("Error connecting to database:")
    else:
        myQry="SELECT * FROM sales;"

        myCursor = mycon.cursor()
        myCursor.execute(myQry)

        salesInfo = myCursor.fetchall()
        if salesInfo==None:
            print("Sales Details Not Found")
        else:
            for oneSales in salesInfo:
                print("     ",oneSales)
        mycon.close()

def selectCustomerIDInSales():
    mycon=connector.connect(host='localhost', user='root', password='Eagleseye@512',database='rdbms_project_sem3',
                            auth_plugin='mysql_native_password')
    if mycon.is_connected == False:
        print("Error connecting to database:")
    else:
        cname = input("Enter customer's name who's customer ID has to be searched: ")
        myQry="SELECT cid FROM customer WHERE cname='"+cname+"'"+";"

        myCursor = mycon.cursor()
        myCursor.execute(myQry)

        cusInfo=myCursor.fetchone()
        if cusInfo==None:
            print("Customer Details Not Found")
        else:
            print("     List Of Customer ID's       ")
            print("Customer ID     Customer Name    ")
            for oneCustomer in cusInfo:
                print("     ", oneCustomer)
        mycon.close()

def selectGoodsIDInSales():
    mycon=connector.connect(host='localhost', user='root', password='Eagleseye@512',database='rdbms_project_sem3',
                            auth_plugin='mysql_native_password')
    if not mycon.is_connected:
        print("Error connecting to database:")
    else:
        myQry="SELECT gid FROM sales"

        myCursor = mycon.cursor()
        myCursor.execute(myQry)

        goodsInfo=myCursor.fetchone()
        if goodsInfo==None:
            print("Goods Details Not Found")
        else:
            print("Goods ID     ")
            for oneGoods in goodsInfo:
                print("     ", oneGoods)
        mycon.close()

def selectSalesDate():
    mycon=connector.connect(host='localhost', user='root', password='Eagleseye@512',database='rdbms_project_sem3',
                            auth_plugin='mysql_native_password')
    if mycon.is_connected == False:
        print("Error connecting to database:")
    else:
        salesid=input("Enter sales ID who's selling date has to be searched: ")
        myQry="SELECT salesdate FROM sales WHERE salesid="+salesid+";"

        myCursor = mycon.cursor()
        myCursor.execute(myQry)

        cusInfo = myCursor.fetchone()
        if cusInfo==None:
            print("Sales Date Not Found")
        else:
            print("     Sales Date:       ")
            for oneSales in cusInfo:
                print("     ", oneSales)
        mycon.close()

def selectSalesQuantity():
    mycon=connector.connect(host='localhost', user='root', password='Eagleseye@512',database='rdbms_project_sem3',
                            auth_plugin='mysql_native_password')
    if mycon.is_connected == False:
        print("Error connecting to database:")
    else:
        salesid=input("Enter sales ID who's selling date has to be searched: ")
        myQry="SELECT salesqty FROM sales WHERE salesid="+salesid+";"

        myCursor = mycon.cursor()
        myCursor.execute(myQry)

        cusInfo = myCursor.fetchone()
        if cusInfo==None:
            print("Sales Quantity Not Found")
        else:
            print("     Sales Quantity:       ")
            for oneSales in cusInfo:
                print("     ", oneSales)
        mycon.close()



#**************************************REPORTS**************************************




#To calculate daily sales.
def displayDailySales():
    mycon = connector.connect(host='localhost', user='root', password='Eagleseye@512', database='rdbms_project_sem3',
                              auth_plugin='mysql_native_password')
    if mycon.is_connected == False:
        print("Error connecting to database:")
    else:
        date=input("Enter the date whose revenue has to be calculated. (yyyy-mm-dd): ")
        myQry = "SELECT gname,sprice,salesqty,sprice*salesqty As Total FROM sales S, goods G where S.gid=G.gid AND salesdate='"+date+"'"

        myCursor = mycon.cursor()
        myCursor.execute(myQry)
        profit = 0

        dailySalesInfo = myCursor.fetchall()
        if dailySalesInfo == None:
            print("No items sold yet.")
        else:
            print("               Sales Report",date)
            print("     gname       sprice     salesqty     Total")
            for oneSales in dailySalesInfo:
                profit+=oneSales[3]
                print("    ", oneSales[0], "      ", oneSales[1], "    ", oneSales[2],
                      "          ", oneSales[3])
        print("Total revenue made on",date,":", profit)
        mycon.close()


#To calculate daily sales.
def displayMonthlySales():
    mycon = connector.connect(host='localhost', user='root', password='Eagleseye@512', database='rdbms_project_sem3',
                              auth_plugin='mysql_native_password')
    if mycon.is_connected == False:
        print("Error connecting to database:")
    else:
        month=input("Enter the month whose total revenue has to be calculated: ")
        myQry = "SELECT gname,sprice,salesqty,sprice*salesqty As Total FROM sales S, goods G WHERE S.gid=G.gid AND month(salesdate)="+month
        profit = 0
        myCursor = mycon.cursor()
        myCursor.execute(myQry)
        monthL = ["January","February","March","April","May","June","July","August","September","October","November","December"]
        monthlySalesInfo = myCursor.fetchall()
        if monthlySalesInfo == []:
            print("No items sold yet.")
        else:
            print("            Sales Report for",monthL[int(month)-1])
            print("     gname       sprice     salesqty     Total")
            for oneSales in monthlySalesInfo:
                profit += oneSales[3]
                print("    ", oneSales[0], "      ", oneSales[1], "    ", oneSales[2],
                      "          ", oneSales[3])
        print("Total revenue made in", monthL[int(month)-1], ":", profit)
        mycon.close()

#To calculate yearly sales.
def displayYearlySales():
    mycon = connector.connect(host='localhost', user='root', password='Eagleseye@512', database='rdbms_project_sem3',
                              auth_plugin='mysql_native_password')
    if mycon.is_connected == False:
        print("Error connecting to database:")
    else:
        year=input("Enter the year whos total revenue has to be calculated: ")
        myQry = "SELECT gname,sprice,salesqty,sprice*salesqty As Total FROM sales S, goods G WHERE S.gid=G.gid AND year(salesdate)="+year
        myCursor = mycon.cursor()
        myCursor.execute(myQry)
        profit=0
        yearlySalesInfo = myCursor.fetchall()
        if yearlySalesInfo == []:
            print("No items sold yet.")
        else:
            print("          Sales Report of",year)
            print("     gname       sprice     salesqty     Total")
            for oneSales in yearlySalesInfo:
                profit += oneSales[3]
                print("    ", oneSales[0], "      ", oneSales[1], "    ", oneSales[2],
                      "          ", oneSales[3])
        print("Total revenue made in", year, ":", profit)
        mycon.close()

mainController()