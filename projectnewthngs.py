def custid_validity():
    n=1
    while True:
        cusid=int(input('enter your customer id: '))
        cur.execute('select * from customer_details')
        f=cur.fetchall()
        for i in f:
            if cusid in i:
                n=0
                return(cusid)
                break
            else:
                n+1
        if n!=0:    
            print('THERE IS NO ACCOUNT IN THIS CUSTOMER ID!')
            print('ENTER A VALID CUSTOMER ID OR CREATE A NEW ACCOUNT')

def custname_validity():
    n=0
    while True:
        cusname=input('enter your name: ')
        cur.execute('select * from customer_details')
        f=cur.fetchall()
        for i in f:
            if cusname in i:
                if i[0]==custid: 
                    n=0
                    return(cusname)
                    break
                else:
                    print('ENTER THE NAME GIVEN WHILE CREATING THE ACCOUNT')
            else:
                n+=1
        if n!=0:    
            print('THERE IS NO ACCOUNT IN THIS CUSTOMER NAME!')
            print('ENTER A VALID CUSTOMER NAME OR CREATE A NEW ACCOUNT')

def paswd_validity():
    n=0
    while True:
        pwd=input('enter your password[4 CHARACTERS]: ')
        if len(pwd)==4:
            cur.execute('select * from customer_details')
            f=cur.fetchall()
            for i in f:
                if pwd in i:
                    if i[0]==custid and i[1]==custname:
                        n=0
                        return(pwd)
                        break
                    else:
                        print('INCORRECT PASSWORD')
                else:
                    n+=1
            if n!=0:    
                print('')
                print('ENTER A VALID PASSWORD')
        else:
            print('ENTER YOUR 4 DIGIT PASSWORD')

import mysql.connector
con=mysql.connector.connect(host='localhost',user='root',passwd='Tvsahosur$123',database='online_food_order')
if con.is_connected():
    print(' W E L C O M E    T O    O N L I N E    F O O D    O R D E R I N G    S Y S T E M ')
cur=con.cursor()
custid=custid_validity()
custname=custname_validity()
password=paswd_validity()
print('LOGIN SUCCESSFULL')