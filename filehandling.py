#text files
'''
f=open('filehandling.txt','w')
f.write('jhonny jhonny yes papa\neating sugar no papa\ntelling lies no papa\nopen your mouth ha!ha!haa!')
f.close()

f=open('filehandling.txt','r')
r=f.readlines()
for i in r:
    print(i,end='')



f=open('filehandling.txt','r')
r=f.read(5)
print(r)


f=open('filehandling.txt','r')
r=f.read()
s=r.split()
c=0
for i in s:
    c+=1
print(c)


f=open('filehandling.txt','r')
r=f.read()
s=r.split()
l=0
lw=''
for i in s:
    if len(i)>l:
        lw=i
        l=len(i)
print(lw)
print(len(lw))


f=open('filehandling.txt','r')
r=f.read()
c=0
for i in r:
    if i in 'aeiouAEIOU':
        c+=1
print(c)


f=open('filehandling.txt','r')
r=f.read()
c=0
for i in r:
    if i in'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        c+=1
print(c)


f=open('filehandling.txt','r')
r=f.read()
c=0
s=r.split()
for i in s:
    if i=='papa':
        c+=1
print(c)


f=open('filehandling.txt','r')
r=f.readline()
print(r)

f=open('filehandling.txt','r')
r=f.readlines()
le=0
ls=[]
for i in r:
    if len(i)>le:
        ls=i
        le=len(i)
print(ls,le)

f=open('filehandling.txt','r')
r=f.readlines()
print(len(r))


r=f=open('filehandling.txt','r')
r=f.readlines()
c=0
for i in r:
    if i[0]=='j':
        c+=1
print(c)


f=open('filehandling.txt','r')
r=f.readlines()
for i in range(len(r)):
    if i%2==0:
        print(r[i],end='')

f=open('filehandling.txt','r')
r=f.read()
s=r.split()
w=[]
for i in s:
    if len(i)<4:
        w.append(i)
print(w)


f=open('filehandling.txt','r')
r=f.readlines()
nf=[]
for i in r:
    if i[0]=='j':
        nf.append(i)
f1=open('addintonewfile.txt','w')
f1.write(nf[0])
f1.close()

f=open('filehandling.txt','r')
r=f.read()
nc=r[::-1]
f1=open('addintonewfile.txt','w')
f1.write(nc)
f1.close()
'''
#binary files
import pickle
'''
f=open('filehandlingb.dat','wb')
r1=['1','abc']
r2=['2','def']
r3=['3','ghi']
r4=['4','jkl']
pickle.dump(r1,f)
pickle.dump(r2,f)
pickle.dump(r3,f)
pickle.dump(r4,f)
f.close()

f=open('filehandlingb.dat','rb')
c=0
try:
    while True:
        r=pickle.load(f)
        print(r)
        c+=1
    
except EOFError:
    print(c)

f=open('filehandlingb.dat','wb')
for i in range(5):
    rno=int(input('enter your rno:'))
    name=input('enter your name:')
    marks=int(input('enter your marks:'))
    l=[rno,name,marks]
    pickle.dump(l,f)
f.close()


f=open('filehandlingb.dat','wb')
for i in range (5):
    furnitureid=int(input('enter the id:'))
    fname=input('enter the name:')
    fprice=int(input('enter the price:'))
    print('furnitureid,fname,fprice')
    l=[furnitureid,fname,fprice]
    pickle.dump(l,f)
f.close()

f=open('filehandlingb.dat','rb')
try:
    while True:
        r=pickle.load(f)
        print(r)
except EOFError:
    print('end')

f=open('filehandlingb.dat','rb')
try:
    while True:
            r=pickle.load(f)
            if r[2]>10000:
                print(r)
except EOFError:
    print('end')


f=open('filehandlingb.dat','rb')
try:
    l=[]
    while True:
        r=pickle.load(f)
        print(r)
        if r[0]!=2:
            l.append(r)
        else:
            continue
    
    f.close()
    
except EOFError:
    print('end')

f=open('filehandlingb.dat','wb')
pickle.dump(l,f)
f.close()
'''

#CSV Files
f=open('filehandlingcsv.csv','w',newline='')
wr=csv.writter(f)
for i in range(2):
    l=csv.writerows[]
