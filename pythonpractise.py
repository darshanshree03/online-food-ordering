'''
list1=[10,25,35,0,10,20]
l=l.sort()
print(l[1])


l=[10,25,35,10,0,20]
print(l)
n=int(input('enter a number from the above list:'))
i=l.index(n)
print(i)


l=[10,25,35,10,0,20]
print(l)
i=0
while i==0:
    print('enter 1 if you want to add items into the list;')
    print('enter-1 if you want to remove items from the list:')
    a=int(input('enter your decision:'))
    if a==1:
        n=int(input('enter the number you want to add:'))
        l.append(n)
        print(l)
        print('do you want to continue? if yes print 2 else print 0')
        c=int(input('want to continue?'))
        if c==2:
            continue
        else:
            break
    elif a==-1:
        n=int(input('enter the number you want to remove:'))
        l.remove(n)
        print(l)
        print('do you want to continue? if yes print 2 else print 0')
        c=int(input('want to continue?'))
        if c==2:
            continue
        else:
            break
    else:
        print('enter a valid number')


l=[10,25,35,10,0,20]
l.sort()
print(l)


l=[10,25,35,10,0,20]
l.reverse()
print(l)


l=['this','is','a','list','a','a','having','one','and','only','strings','throughout','the','list']
c=l.count('list')
print(c)


i=0
while i==0:
    print('if you want to add any numbers enter + (or) if you want to subtract any number enter - (or) if you want to divide any number enter % (or) if you want to multiply any number enter x')
    m=input('mathematical operation:')
    if m=='+':
        a1=int(input('enter the number:'))
        a2=int(input('enter the number:'))
        print(a1+a2)
        print('if you wan to continue calculating enter s else n')
        c=input('want to vontinue?')
        if c=='s':
            continue
        else:
            break
    elif m=='-':
        a1=int(input('enter the number:'))
        a2=int(input('enter the number:'))
        print(a1-a2)
        print('if you wan to continue calculating enter s else n')
        c=input('want to vontinue?')
        if c=='s':
            continue
        else:
            break
    elif m=='%':
        a1=int(input('enter the number:'))
        a2=int(input('enter the number:'))
        print(a1/a2)
        print('if you wan to continue calculating enter s else n')
        c=input('want to vontinue?')
        if c=='s':
            continue
        else:
            break
    elif m=='x':
        a1=int(input('enter the number:'))
        a2=int(input('enter the number:'))
        print(a1*a2)
        print('if you wan to continue calculating enter s else n')
        c=input('want to vontinue?')
        if c=='s':
            continue
        else:
            break


s=input('enter a string:')
l=s.split()
c=0
for i in range (0,len(l)):
    if l[i][0]=='m' or l[i][0]=='M':
        c+=1
    else:
        continue
print(c)
'''        
