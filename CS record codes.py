#INTERFACING CODES
'''
#6
import mysql.connector
con=mysql.connector.connect(host='localhost',user='root',password='Tvsahosur$123',database='record')
if con.is_connected():
    print('successfully connected')
cur=con.cursor()
cur.execute('select * from account')
data= cur.fetchall()
count=cur.rowcount
for i in data:
    print(i)
con.close()

#7
import mysql.connector
con=mysql.connector.connect(host='localhost',user='root',password='Tvsahosur$123',database='cs_record')
if con.is_connected():
    print('successfully connected')
cur=con.cursor()
n=input('enter the acc no:')
a=input('enter the address:')
e="update accounts set address='{}' where ano='{}'".format(a,n)
cur.execute(e)
con.commit()

#8
import mysql.connector
con=mysql.connector.connect(host='localhost',user='root',password='Tvsahour$123',database='record')
if con.is_connected():
    print('successfully connected')
cur=con.cursor()
cur.execute("select * from accounts where address='%s'" %('Chennai'))
data= cur.fetchall()
count=cur.rowcount
for i in data:
    print(i)
con.close()

#9
import mysql.connector
con=mysql.connector.connect(host='localhost',user='root',password='Tvsahosur$123',database='record')
if con.is_connected():
    print('successfully connected')
cur=con.cursor()
col= input('enter column name: ')
rec= input('enter the record: ')
cur.execute("select * from account where {}='{}'".format(col,rec))
data= cur.fetchall()
count=cur.rowcount
for i in data:
    print(i)
con.close()
'''

#PYTHON,STACKS AND FILE HANDLING
'''
#10
def assign():
    for i in range(80):
        print('=',end='')
    print('enter (1) if you want to find the factorial')
    print('enter (2) if you want to check amstrong number')
    print('enter (3) to check the number is prime or not')
    print('enter (4) to kill the program')
    for i in range(80):
        print('=',end='')

def ck():
    for i in range(80):
        print('=',end='')
    print('enter (s) if you want to continue the program')
    print('enter (n) if you want to kill the program')
    for i in range(80):
        print('=',end='')
        
def fact(x):
    c=1
    for i in range(1,n+1):
       c=c*i
    return(c)

def armstrong(x):
    l=len(str(x))
    a=0
    while (x>0):
        d=x%10
        a+=d**l
        x=x//10
    if a==n:
        print('yes',n,'is an amstrong number')
    else:
        print('no',n,'is not an amstrong number')

def prime(n):
    for i in range(2,n):
        if n%i==0:
            c=0
            return(c)
            
#MAIN BLOCK                
while True:
    assign()
    c=int(input('enter your choice: '))
    if c==1:
        n=int(input('enter the number to find the factorial: '))
        print('the factorial of the given number is:', fact(n))
    elif c==2:
        n=int(input('enter the number: '))
        armstrong(n)
    elif c==3:
        n=int(input('enter the number:'))
        if prime(n)==0:
            print(n,'is a composite number')
        else:
            print(n,'is a prime number')
    elif c==4:
        print('THANK YOU')
        break
    else:
        print('enter a valid number')
    ck()
    k=input('still wanna continue?' )
    if k=='n':
        print('THANK YOU')
        break
'''
#11

n1=input('enter a word: ')
n2=input('enter a word: ')
fw=n1.split()
sw=n2.split()
print(fw)
if len(n1)==len(n2):
    for i in range (len(n1)):
        if fw[i] in sw:
            print('the words are anagram')

else: 
    print('the word is not an anagram')







'''
#16

def pres():
    for i in range (80):
        print('=',end='')
def impl():
    print('enter (1) if you want to add element to the list \nenter (2) if you want to remove the last element from the list\nenter (3) if you want to display the last element from the list\n enter(4) if you want to exit the program')
    pres()
    c=int(input('enter your choice:'))
    return(c)
def push(x):
    l.append(x)
def pop():
    p=l.pop()
    return p
def display():
    top=-1
    return(l[top])
    
l=[]
while True:
    i=impl()
    if i==1:
        a=int(input('enter the number you want to add:'))
        push(a)
        pres()
    elif i==2:
        x=pop()
        if x=='underflow':
            print('stack is empty')
            pres()
        else:
            print('the deleted element is:',x)
            pres()
    elif i==3:
        if x=='underflow':
            print('the stak is empty')
            pres()
        else:
            print('the last element is:',display())
            pres()
    elif i==4:
            print('THANK YOU!!')
            pres()
            break
    else:
        print('select an appropriate number')
        impl()
        continue
    print('enter (s) if you want to continue\nenter (n) if you want to exit')
    pres()
    e=input('enter your choice:')
    if e=='n':
        break
    elif e=='s':
        continue
    else:
        print('select the correct alphabet')

#17

def push(a):
    l.append(a)

def pop():
    p=l.pop()
    return(p)

def disp():
    top=-1
    return(l[top])

l=[]
while True:
    n=int(input('enter the number to add:'))
    for i in range(80):
        print('=',end='')
    if n%5==0:
        push(n)
    print('enter (1) if you want to delete the last ellement from the stack\nenter (2) if you want to display the last element from the stack')
    for i in range(80):
        print('=',end='')
    c=int(input('enter your choice:'))
    if c==1:
        a=pop()
        if a=='underflow':
            print('the stack is empty')
            for i in range(80):
                print('=',end='')
        else:
            print('the last element deleted is:',a)
            for i in range(80):
                print('=',end='')
    elif c==2:
        if disp()=='underflow':
            print('the stack is empty')
            for i in range(80):
                print('=',end='')
        else:
            print('the last element in the stack is:', disp())
            for i in range(80):
                print('=',end='')
    else:
        print('enter the appropriate number')
        for i in range(80):
                print('=',end='')

        
#18

f=open('praticalfile.txt','r')
r=f.read()
s=r.split()
c=0
for i in s:
    for j in range (len(i)):  
        if i[j].isupper():
            c=c+1
        else:
            continue
print('no. of uppercase in the text are:',c)
f.close()


#19

f=open('praticalfile.txt','r')
r=f.read()
s=r.split()
c=0
l=[]
for i in s:
    if len(i)<4:
        l.append(i)
    else:
        continue
print('no. of words having letters less than 4 is',l)
f.close()


#20

f=open('praticalfile.txt','r')
r=f.readlines()
l=[]
c=0
for i in r:
    if i[0]=='M':
        l.append(i)
        c+=1
    else:
        continue
print("number of M's are:",c)
print("the sentences are:",l)


f=open('chummaadd.txt','w')
for j in l:
    f.write(j)

f.close()

#21

f=open('praticalfile.txt','r')
r=f.read()
s=r.split()
d={}
for i in s:
    c=s.count(i)
    d[i]=c
print(d)

#22

import pickle
f=open('praticalfileb.dat','wb')
det={}
for i in range (2):
    r=int(input('enter the roll number:'))
    n=input('enter the name:')
    det['rollno']=r
    det['name']=n
    pickle.dump(det,f)
f.close()
f=open('praticalfileb.dat','rb')
s=int(input('enter the roll number you want to search:'))
try:
    while True:
        a=pickle.load(f)
        if a['rollno']==s:
            print(a)
            break
except EOFError:
    print('sorry, the roll number is not found in the record')
f.close()

#23

import pickle
f=open('particalfile.dat','wb')
d={}
for i in range(3):
    no=int(input('enter the employee number:'))
    n=input('enter the name:')
    des=input('enter your designation:')
    d['eno']=no
    d['ename']=n
    d['designation']=des
    pickle.dump(d,f)
f.close()
f=open('praticalfile.dat','wb+')
c=int(input('enter the eno you want to update:'))
print('enter (1) if you want to update the eno\n enter (2) if you want to update name\n enter(3) if you want to update the designation')
e=int(input('enter the number:'))
for i in range 1:
    if e==1:
        u=int(input('update the eno to:'))
        break
    elif e==2:
        u=input('update the ename to:')
    elif e==3:
        u=input('update the designation to:')
'''