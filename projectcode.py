def welcome():
    print('='*80)
    print('enter (1) to CREATE A NEW ACCOUNT')
    print('enter (2) to LOGIN')
    print('enter (3) to REPORT')
    print('enter (4) to EXIT')
    print('='*80)

def login():
    print('*'*80)
    print('enter (1) to VIEW CUSTOMER DETAILS')
    print('enter (2) to UPDATE CUSTOMER DETAILS')
    print('enter (3) to ORDER FOOD')
    print('enter (4) to EXIT')
    print('*'*80)

def login_update():
    print()
    print('enter 1 if you want to UPDATE YOUR NAME')
    print('enter 2 if you want to UPDATE YOUR PHONE NUMBER')
    print('enter 3 if you want to UPDATE YOUR EMAIL')
    print('enter 4 if you want to UPDATE YOUR ADDRESS')
    print('enter 5 if you want to UPDATE YOUR PASSWORD')
    print('='*80)

def order_menu():
    print('='*80)
    print('enter (1) if you want to order STARTERS')
    print('enter (2) if you want to order BREAKFAST')
    print('enter (3) if you want to order LUNCH')
    print('enter (4) if you want to order DINNER')
    print('enter (5) if you want to order BEVARAGES')
    print('enter (6) if you want to order DESSERTS')
    print('='*80)

def order_meth():
    print('enter T to takeaway your order')
    print('enter S to eat it here')
    print('enter D to door deliever your order')

def email_validity():
    while True:
        em=input('enter your email id: ')
        if '@' in em:
            if '.' in em:
                if em[-4]=='.':
                    return (em)
                    break
                else:
                    print('INVALID EMAIL FORMAT!')
            else:
                print("Dot(.) missing in the mail id")
        else:
            print("@ missing in mail id")

def phnumber_validity():
    while True:
        phone=input('enter your phone number:')
        if len(phone)== 10:
            if phone.isdigit():
                if phone[0]!='0':
                    return(phone)
                    break
                else:
                    print('YOUR PHONE NUMBER CANNOT START WITH ZERO(0)')
            else:
                print('YOUR PHONE NUMBER SHOULD NOT CONTAIN ANY ALPHABETS OR SPECIAL CHARACTERS!')
        else:
            print('YOUR PHONE NUMBER SHOULD CONTAIN 10 DIGITS!')
    
def passwd_validity():
    while True:
        passwd=input('enter your four digit pin: ')
        if len(passwd)==4:
            if passwd.isdigit():
                return(passwd)
                break
            else:
                print('ENTER ONLY NUMBERS')
        else:
            print('ENTER ONLY 4 CHARACTERS')

def order():
    def order_menu():
        print('='*80)
        print('enter (1) if you want to order STARTERS')
        print('enter (2) if you want to order BREAKFAST')
        print('enter (3) if you want to order LUNCH')
        print('enter (4) if you want to order DINNER')
        print('enter (5) if you want to order BEVARAGES')
        print('enter (6) if you want to order DESSERTS')
        print('='*80)

    def order_cntnu():
        print('ENTER (Y) TO CONTINUE YOUR ORDER')
        print('ENTER (N) TO EXIT ORDERING AND PAY FOR THE ORDER')
        

    #STARTERS
    def starters():
        def soups():
            print('                          SOUPS                       ')
            print('    |',end='')
            print('='*53)
            print('    | FOOD NUMBER   |     FOOD NAME      |   PRICE   |')
            print('    |',end='')
            print('-'*53)
            print('    |      01s      |   baby corn soup   |   Rs.80   |')
            print('    |      02s      |   mushroom soup    |   Rs.80   |')
            print('    |      03s      |   tomato soup      |   Rs.70   |')
            print('    |      04s      |   veg soup         |   Rs.80   |')
            print('    ',end='')
            print('='*54)
            print('')

        def chats():
            print('                           CHATS                           ')
            print('    |',end='')
            print('='*53)
            print('    | FOOD NUMBER   |      FOOD NAME           |  PRICE   |')
            print('    |',end='')
            print('-'*53)
            print('    |      05s      |   baby corn manchurian   |  Rs.90   |')
            print('    |      06s      |   panner manchurian      |  Rs.90   |')
            print('    |      07s      |   gopi manchurian        |  Rs.70   |')
            print('    |      08s      |   mushroom manchurian    |  Rs.90   |')
            print('    |      09s      |   panner samosa          |  Rs.30   |')
            print('    |      10s      |   mushroom samosa        |  Rs.30   |')
            print('    |      11s      |   onion samosa           |  Rs.20   |')
            print('    |      12s      |   potato samosa          |  Rs.20   |')
            print('    |      13s      |   noodles samosa         |  Rs.30   |')
            print('    |      14s      |   onion pakoda           |  Rs.30   |')
            print('    |      15s      |   medhu vadai            |  Rs.20   |')
            print('    |      16s      |   masal vadai            |  Rs.10   |')
            print('    ',end='')
            print('='*54)
            print('')

        def starters_order(qs):
            chckp='select price from starters where foodid=%s'
            ms=(msv,)
            cur.execute(chckp,ms)
            fetch_price=cur.fetchone()
            fpint=int(fetch_price[0])
            p=fpint*qs
            global bill
            bill+=p
        
        def quantityvalidity():
            if str(q) in 'abcdefghijklamnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVW!@#$%^&*()_+=-}{][;:><.,?/|':
                print('enter the valid quantity')
                
        #STARTERS_MAIN
        soups()
        chats()
        itmnos1=input('enter the food numbers to order: ')
        global foodid
        foodid+=itmnos1
        item=itmnos1.split(',')
        cur.execute('select foodid from starters')
        f1=cur.fetchall()
        for s in f1:          
            while s[0] in item:
                if s[0]=='01s':
                    q=int(input('enter the quantity of baby corn soup:'))
                    quantityvalidity()
                    msv='01s'
                    starters_order(q)
                    break
                elif s[0]=='02s':
                    q=int(input('enter the quantity of mushroom soup:'))
                    quantityvalidity()
                    msv='02s'
                    starters_order(q)
                    break
                elif s[0]=='03s':
                    q=int(input('enter the quantity of tomato soup:'))
                    quantityvalidity()
                    msv='03s'
                    starters_order(q)
                    break
                elif s[0]=='04s':
                    q=int(input('enter the quantity of veg soup:'))
                    quantityvalidity()
                    msv='04s'
                    starters_order(q)
                    break
                elif s[0]=='05s':
                    q=int(input('enter the quantity of baby corn manchurian:'))
                    quantityvalidity()
                    msv='05s'
                    starters_order(q)
                    break
                elif s[0]=='06s':
                    q=int(input('enter the quantity of panner manchurian:'))
                    quantityvalidity()
                    msv='06s'
                    starters_order(q)
                    break
                elif s[0]=='07s':
                    q=int(input('enter the quantity of gobi manchurian:'))
                    quantityvalidity()
                    msv='07s'
                    starters_order(q)
                    break
                elif s[0]=='08s':
                    q=int(input('enter the quantity of mushroom manchurian:'))
                    quantityvalidity()
                    msv='08s'
                    starters_order(q)
                    break
                elif s[0]=='09s':
                    q=int(input('enter the quantity of panner samosa:'))
                    quantityvalidity()
                    msv='09s'
                    starters_order(q)
                    break
                elif s[0]=='10s':
                    q=int(input('enter the quantity of mushroom samosa:'))
                    quantityvalidity()
                    msv='10s'
                    starters_order(q)
                    break
                elif s[0]=='11s':
                    q=int(input('enter the quantity of onion samosa:'))
                    quantityvalidity()
                    msv='11s'
                    starters_order(q)
                    break
                elif s[0]=='12s':
                    q=int(input('enter the quantity of potato samosa:'))
                    quantityvalidity()
                    msv='12s'
                    starters_order(q)
                    break
                elif s[0]=='13s':
                    q=int(input('enter the quantity of noodles samosa:'))
                    quantityvalidity()
                    msv='13s'
                    starters_order(q)
                    break
                elif s[0]=='14s':
                    q=int(input('enter the quantity of onion pakoda:'))
                    quantityvalidity()
                    msv='14s'
                    starters_order(q)
                    break
                elif s[0]=='15s':
                    q=int(input('enter the quantity of medhu vadai:'))
                    quantityvalidity()
                    msv='15s'
                    starters_order(q)
                    break
                elif s[0]=='16s':
                    q=int(input('enter the quantity of masal vadai:'))
                    quantityvalidity()
                    msv='16s'
                    starters_order(q)
                    break
    
    #BREAKFAST
    def breakfast():
        print('')
        print('                                 BREAKFAST               ')
        print('    |',end='')
        print('='*72)
        print('    |  FOOD NUMBER  |      FOOD NAME        |   PRICE   |')
        print('    |',end='')
        print('-'*72)
        print('    |      01b      |   idli(3nos)          |   Rs.25   |')
        print('    |      02b      |   kichady             |   Rs.20   |')
        print('    |      03b      |   pongal              |   Rs.25   |')
        print('    |      04b      |   plain dosa          |   Rs.35   |')
        print('    |      05b      |   masal dosa          |   Rs.45   |')
        print('    |      06b      |   rava dosa           |   Rs.45   |')
        print('    |      07b      |   onion dosa          |   Rs.50   |')
        print('    |      08b      |   plain utappam       |   Rs.35   |')
        print('    |      09b      |   onion utappam       |   Rs.45   |')
        print('    |      10b      |   chappati(2nos)      |   Rs.40   |')
        print('    |      11b      |   parota(2nos)        |   Rs.45   |')
        print('    |      12b      |   puttu               |   Rs.45   |')
        print('    |      13b      |   idyapam             |   Rs.45   |')
        print('    |      14b      |   poori(2nos)         |   Rs.45   |')
        print('    |      15b      |   bread toast(2nos)   |   Rs.40   |')
        print('    |      16b      |   veg sandwich        |   Rs.40   |')
        print('    |      17b      |   cheese sandwich     |   Rs.45   |')
        print('    |',end='')
        print('='*72)

        def breakfast_order(qb):
            chckp='select price from breakfast where foodid=%s'
            ms=(msv,)
            cur.execute(chckp,ms)
            fetch_price=cur.fetchone()
            fpint=int(fetch_price[0])
            p=fpint*qb
            global bill
            bill+=p

        def chckquantity():
            if str(q) in 'abcdefghijklamnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVW!@#$%^&*()_+=-}{][;:><.,?/|':
                print('enter the valid quantity:')

        #BREAKFAST_MAIN
        itmnos2=input('enter the food numbers to order: ')
        global foodid
        foodid+=itmnos2
        item=itmnos2.split(',')
        cur.execute('select foodid from breakfast')
        f1=cur.fetchall()
        for b in f1:          
            while b[0] in item:
                if b[0]=='01b':
                    q=int(input('enter the quantity of idli:'))
                    chckquantity()
                    msv='01b'
                    breakfast_order(q)
                    break
                if b[0]=='02b':
                    q=int(input('enter the quantity of kichady:'))
                    chckquantity()
                    msv='02b'
                    breakfast_order(q)
                    break
                if b[0]=='03b':
                    q=int(input('enter the quantity of pongal:'))
                    chckquantity()
                    msv='03b'
                    breakfast_order(q)
                    break
                if b[0]=='41b':
                    q=int(input('enter the quantity of plain dosa:'))
                    chckquantity()
                    msv='04b'
                    breakfast_order(q)
                    break
                if b[0]=='05b':
                    q=int(input('enter the quantity of masal dosa:'))
                    chckquantity()
                    msv='05b'
                    breakfast_order(q)
                    break
                if b[0]=='06b':
                    q=int(input('enter the quantity of rava dosa:'))
                    chckquantity()
                    msv='06b'
                    breakfast_order(q)
                    break
                if b[0]=='07b':
                    q=int(input('enter the quantity of onion dosa:'))
                    chckquantity()
                    msv='07b'
                    breakfast_order(q)
                    break
                if b[0]=='08b':
                    q=int(input('enter the quantity of plain utapam:'))
                    chckquantity()
                    msv='08b'
                    breakfast_order(q)
                    break
                if b[0]=='09b':
                    q=int(input('enter the quantity of onion utapam:'))
                    chckquantity()
                    msv='09b'
                    breakfast_order(q)
                    break
                if b[0]=='10b':
                    q=int(input('enter the quantity of chapati:'))
                    chckquantity()
                    msv='10b'
                    breakfast_order(q)
                    break
                if b[0]=='11b':
                    q=int(input('enter the quantity of parota:'))
                    chckquantity()
                    msv='11b'
                    breakfast_order(q)
                    break
                if b[0]=='12b':
                    q=int(input('enter the quantity of puttu:'))
                    chckquantity()
                    msv='12b'
                    breakfast_order(q)
                    break
                if b[0]=='13b':
                    q=int(input('enter the quantity of idiyapam:'))
                    chckquantity()
                    msv='13b'
                    breakfast_order(q)
                    break
                if b[0]=='14b':
                    q=int(input('enter the quantity of poori:'))
                    chckquantity()
                    msv='14b'
                    breakfast_order(q)
                    break
                if b[0]=='15b':
                    q=int(input('enter the quantity of bread toast:'))
                    chckquantity()
                    msv='15b'
                    breakfast_order(q)
                    break
                if b[0]=='16b':
                    q=int(input('enter the quantity of vef sandwich:'))
                    chckquantity()
                    msv='16b'
                    breakfast_order(q)
                    break
                if b[0]=='17b':
                    q=int(input('enter the quantity of cheese sandwich:'))
                    chckquantity()
                    msv='17b'
                    breakfast_order(q)
                    break

    #LUNCH
    def lunch():
        print('')
        print('                                 LUNCH                          ')
        print('    |',end='')
        print('-'*72)
        print('    |  FOOD NUMBER  |        FOOD NAME             |   PRICE   |')
        print('    |',end='')
        print('-'*72)
        print('    |      01l      |   pongal                     |   Rs.25   |')
        print('    |      02l      |   kichady                    |   Rs.20   |')
        print('    |      03l      |   chapati(2nos)              |   Rs.40   |')
        print('    |      04l      |   aloo paratha               |   Rs.45   |')
        print('    |      05l      |   veg noodles                |   Rs.30   |')
        print('    |      06l      |   gobi noodles               |   Rs.45   |')
        print('    |      07l      |   msuhroom noodles           |   Rs.45   |')
        print('    |      08l      |   mini meals                 |   Rs.40   |')
        print('    |      09l      |   meals                      |   Rs.50   |')
        print('    |      10l      |   veg biriyani               |   Rs.45   |')
        print('    |      11l      |   mushroom biriyani          |   Rs.45   |')
        print('    |      12l      |   veg fried rice             |   Rs.45   |')
        print('    |      13l      |   chilli garlic fried rice   |   Rs.50   |')
        print('    |      14l      |   spicy cottage fried rice   |   Rs.50   |')
        print('    |      15l      |   panner fried rice          |   Rs.45   |')
        print('    |      16l      |   baby corn rice             |   Rs.45   |')
        print('    |      17l      |   gobi rice                  |   Rs.40   |')
        print('    |      18l      |   jeera rice                 |   Rs.40   |')
        print('    |      19l      |   ghee rice                  |   Rs.40   |')
        print('    |      20l      |   peas pulao                 |   Rs.40   |')
        print('    |      21l      |   puliogare                  |   Rs.35   |')
        print('    |',end='')
        print('='*72)


        def lunch_order(ql):
            chckp='select price from lunch where foodid=%s'
            ms=(msv,)
            cur.execute(chckp,ms)
            fetch_price=cur.fetchone()
            fpint=int(fetch_price[0])
            p=fpint*ql
            global bill
            bill+=p

        def chckquantity():
            if str(q) in 'abcdefghijklamnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVW!@#$%^&*()_+=-}{][;:><.,?/|':
                print('enter the valid quantity:')

        #LUNCH_MAIN
        itmnos3=input('enter the food numbers to order: ')
        global foodid
        foodid+=itmnos3
        item=itmnos3.split(',')
        cur.execute('select foodid from lunch')
        f1=cur.fetchall()
        for l in f1:          
            while l[0] in item:
                if l[0]=='01l':
                    q=int(input('enter the quantity of pongal:'))
                    chckquantity()
                    msv='01l'
                    lunch_order(q)
                    break
                if l[0]=='02l':
                    q=int(input('enter the quantity of kichady:'))
                    chckquantity()
                    msv='02l'
                    lunch_order(q)
                    break
                if l[0]=='03l':
                    q=int(input('enter the quantity of chapati:'))
                    chckquantity()
                    msv='03l'
                    lunch_order(q)
                    break
                if l[0]=='04l':
                    q=int(input('enter the quantity of aloo paratha:'))
                    chckquantity()
                    msv='04l'
                    lunch_order(q)
                    break
                if l[0]=='05l':
                    q=int(input('enter the quantity of veg noodles:'))
                    chckquantity()
                    msv='05l'
                    lunch_order(q)
                    break
                if l[0]=='06l':
                    q=int(input('enter the quantity of gobi noodles:'))
                    chckquantity()
                    msv='06l'
                    lunch_order(q)
                    break
                if l[0]=='07l':
                    q=int(input('enter the quantity of mushroom noodles:'))
                    chckquantity()
                    msv='07l'
                    lunch_order(q)
                    break
                if l[0]=='08l':
                    q=int(input('enter the quantity of mini meals:'))
                    chckquantity()
                    msv='08l'
                    lunch_order(q)
                    break
                if l[0]=='09l':
                    q=int(input('enter the quantity of meals:'))
                    chckquantity()
                    msv='09l'
                    lunch_order(q)
                    break
                if l[0]=='10l':
                    q=int(input('enter the quantity of veg biriyani:'))
                    chckquantity()
                    msv='10l'
                    lunch_order(q)
                    break
                if l[0]=='11l':
                    q=int(input('enter the quantity of mushroom biriyani:'))
                    chckquantity()
                    msv='11l'
                    lunch_order(q)
                    break
                if l[0]=='12l':
                    q=int(input('enter the quantity of veg fried rice:'))
                    chckquantity()
                    msv='12l'
                    lunch_order(q)
                    break
                if l[0]=='13l':
                    q=int(input('enter the quantity of chilli garlic fried rice:'))
                    chckquantity()
                    msv='13l'
                    lunch_order(q)
                    break
                if l[0]=='14l':
                    q=int(input('enter the quantity of spicy cottage fried rice:'))
                    chckquantity()
                    msv='14l'
                    lunch_order(q)
                    break
                if l[0]=='15l':
                    q=int(input('enter the quantity of panner fried rice:'))
                    chckquantity()
                    msv='15l'
                    lunch_order(q)
                    break
                if l[0]=='16l':
                    q=int(input('enter the quantity of baby corn rice:'))
                    chckquantity()
                    msv='16l'
                    lunch_order(q)
                    break
                if l[0]=='17l':
                    q=int(input('enter the quantity of gobi rice:'))
                    chckquantity()
                    msv='17l'
                    lunch_order(q)
                    break
                if l[0]=='18l':
                    q=int(input('enter the quantity of jeera rice:'))
                    chckquantity()
                    msv='18l'
                    lunch_order(q)
                    break
                if l[0]=='19l':
                    q=int(input('enter the quantity of ghee rice:'))
                    chckquantity()
                    msv='19l'
                    lunch_order(q)
                    break
                if l[0]=='20l':
                    q=int(input('enter the quantity of peas pulao:'))
                    chckquantity()
                    msv='20l'
                    lunch_order(q)
                    break
                if l[0]=='21l':
                    q=int(input('enter the quantity of puliogare:'))
                    chckquantity()
                    msv='21l'
                    lunch_order(q)
                    break
    
    #DINNER
    def dinner():
        print('                          DINNER                         ')
        print('')
        print('')
        print('                    DOSA VARIETIES                       ')
        print('    |',end='')
        print('-'*72)
        print('    |  FOOD NUMBER  |     FOOD NAME         |   PRICE    |')
        print('    |',end='')
        print('-'*72)
        print('    |      01d      |   plain dosa          |   Rs.60    |')                 
        print('    |      02d      |   masal dosa          |   Rs.70    |')
        print('    |      03d      |   ghee dosa           |   Rs.70    |')
        print('    |      04d      |   ghee masal dosa     |   Rs.80    |')
        print('    |      05d      |   rava dosa           |   Rs.70    |')
        print('    |      06d      |   podi dosa           |   Rs.60    |')
        print('    |      07d      |   onion dosa          |   Rs.70    |')
        print('    |      08d      |   mysore masal dosa   |   Rs.90    |')
        print('    |      09d      |   gobi dosa           |   Rs.90    |')
        print('    |      10d      |   mushroom dosa       |   Rs.100   |')
        print('    |      11d      |   baby corn dosa      |   Rs.100   |')
        print('    |      12d      |   uthappam            |   Rs.50    |')
        print('    |      13d      |   onion uthappam      |   Rs.60    |')
        print('    |      14d      |   aapam               |   Rs.50    |')
        print('    |',end='')
        print('='*72)
        print('')
        print('                    ROTIS AND NAANS                  ')
        print('    |',end='')
        print('-'*72)
        print('    |  FOOD NUMBER  |   FOOD NAME       |   PRICE   |')
        print('    |',end='')
        print('-'*72)
        print('    |      15d      |   plain naan      |   Rs.50   |')
        print('    |      16d      |   butter naan     |   Rs.60   |')
        print('    |      17d      |   garlic naan     |   Rs.60   |')
        print('    |      18d      |   kultcha         |   Rs.50   |')
        print('    |      19d      |   aalo paratha    |   Rs.60   |')
        print('    |      20d      |   chilli parota   |   Rs.70   |')
        print('    |      21d      |   parota          |   Rs.45   |')               
        print('    |      22d      |   chapati         |   Rs.40   |')
        print('    |      23d      |   poori           |   Rs.50   |')
        print('    |      24d      |   chola poori     |   Rs.70   |')
        print('    |',end='')
        print('='*72)
        print('')
        print('                          GRAVY ITEMS                        ')
        print('    |',end='')
        print('-'*72)
        print('    |  FOOD NUMBER  |   FOOD NAME              |   PRICE    |')
        print('    |',end='')
        print('-'*72)
        print('    |      25d      |   dhal fry               |   Rs.90    |')
        print('    |      26d      |   dhal palak             |   Rs.90    |')
        print('    |      27d      |   mix veg curry          |   Rs.95    |')
        print('    |      28d      |   panner butter masala   |   Rs.120   |')
        print('    |      29d      |   green peas masala      |   Rs.105   |')
        print('    |      30d      |   panner tikka masala    |   Rs.125   |')
        print('    |      31d      |   kadai panner           |   Rs.120   |')
        print('    |      32d      |   kadai mushroom         |   Rs.120   |')
        print('    |      33d      |   chenna masala          |   Rs.105   |')
        print('    |      34d      |   malai kufhta           |   Rs.110   |')
        print('    |      35d      |   veg kufhta             |   Rs.115   |')
        print('    |',end='')
        print('='*72)
        print('')
        print('                    RICE AND NOODLES                      ')
        print('    |',end='')
        print('-'*72)
        print('    |  FOOD NUMBER  |       FOOD NAME         |   PRICE    |')
        print('    |',end='')
        print('-'*72)
        print('    |      36d      |   veg noodles           |   Rs.100    |')
        print('    |      37d      |   mushroom noodles      |   Rs.145    |')
        print('    |      38d      |   szeschwan noodles     |   Rs.115    |')
        print('    |      39d      |   veg fried rice        |   Rs.105    |')
        print('    |      40d      |   mushroom fried rice   |   Rs.125    |')
        print('    |      41d      |   jeera rice            |   Rs.105    |')
        print('    |      42d      |   ghee rice             |   Rs.105    |')
        print('    |      43d      |   veg pulav             |   Rs.115    |')
        print('    |      44d      |   garlic fries rice     |   Rs.100    |')
        print('    |      45d      |   szechwan fried rice   |   Rs.125    |')
        print('')
        def dinner_order(qd):
            chckp='select price from dinner where foodid=%s'
            ms=(msv,)
            cur.execute(chckp,ms)
            fetch_price=cur.fetchone()
            fpint=int(fetch_price[0])
            p=fpint*qd
            global bill
            bill+=p

        def chckquantity():
            if str(q) in 'abcdefghijklamnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVW!@#$%^&*()_+=-}{][;:><.,?/|':
                print('enter the valid quantity:')


        #DINNER_MAIN
        itmnos4=input('enter the food numbers to order: ')
        global foodid
        foodid+=itmnos4
        item=itmnos4.split(',')
        cur.execute('select foodid from dinner')
        f1=cur.fetchall()
        for d in f1:          
            while d[0] in item:
                if d[0]=='01d':
                    q=int(input('enter the quantity of plain dosa:'))
                    chckquantity()
                    msv='01d'
                    dinner_order(q)
                    break
                if d[0]=='02d':
                    q=int(input('enter the quantity of masla dosa:'))
                    chckquantity()
                    msv='02d'
                    dinner_order(q)
                    break
                if d[0]=='03d':
                    q=int(input('enter the quantity of ghee dosa:'))
                    chckquantity()
                    msv='03d'
                    dinner_order(q)
                    break
                if d[0]=='04d':
                    q=int(input('enter the quantity of ghee masal dosa:'))
                    chckquantity()
                    msv='04d'
                    dinner_order(q)
                    break
                if d[0]=='05d':
                    q=int(input('enter the quantity of rava dosa:'))
                    chckquantity()
                    msv='05d'
                    dinner_order(q)
                    break
                if d[0]=='06d':
                    q=int(input('enter the quantity of podi dosa:'))
                    chckquantity()
                    msv='06d'
                    dinner_order(q)
                    break
                if d[0]=='07d':
                    q=int(input('enter the quantity of onion dosa:'))
                    chckquantity()
                    msv='07d'
                    dinner_order(q)
                    break
                if d[0]=='08d':
                    q=int(input('enter the quantity of mysore masal dosa:'))
                    chckquantity()
                    msv='08d'
                    dinner_order(q)
                    break
                if d[0]=='09d':
                    q=int(input('enter the quantity of gobi dosa:'))
                    chckquantity()
                    msv='09d'
                    dinner_order(q)
                    break
                if d[0]=='10d':
                    q=int(input('enter the quantity of mushroom dosa:'))
                    chckquantity()
                    msv='10d'
                    dinner_order(q)
                    break
                if d[0]=='11d':
                    q=int(input('enter the quantity of baby corn dosa:'))
                    chckquantity()
                    msv='11d'
                    dinner_order(q)
                    break
                if d[0]=='12d':
                    q=int(input('enter the quantity of uthappam:'))
                    chckquantity()
                    msv='12d'
                    dinner_order(q)
                    break
                if d[0]=='13d':
                    q=int(input('enter the quantity of onion uthappam:'))
                    chckquantity()
                    msv='13d'
                    dinner_order(q)
                    break
                if d[0]=='14d':
                    q=int(input('enter the quantity of aapam:'))
                    chckquantity()
                    msv='14d'
                    dinner_order(q)
                    break
                if d[0]=='15d':
                    q=int(input('enter the quantity of plain naan:'))
                    chckquantity()
                    msv='15d'
                    dinner_order(q)
                    break
                if d[0]=='16d':
                    q=int(input('enter the quantity of butter naan:'))
                    chckquantity()
                    msv='16d'
                    dinner_order(q)
                    break
                if d[0]=='17d':
                    q=int(input('enter the quantity of garlic naan:'))
                    chckquantity()
                    msv='17d'
                    dinner_order(q)
                    break
                if d[0]=='18d':
                    q=int(input('enter the quantity of kultcha:'))
                    chckquantity()
                    msv='18d'
                    dinner_order(q)
                    break
                if d[0]=='19d':
                    q=int(input('enter the quantity of aloo paratha:'))
                    chckquantity()
                    msv='19d'
                    dinner_order(q)
                    break
                if d[0]=='20d':
                    q=int(input('enter the quantity of chilli parota:'))
                    chckquantity()
                    msv='20d'
                    dinner_order(q)
                    break
                if d[0]=='21d':
                    q=int(input('enter the quantity of parota:'))
                    chckquantity()
                    msv='21d'
                    dinner_order(q)
                    break
                if d[0]=='22d':
                    q=int(input('enter the quantity of chapati:'))
                    chckquantity()
                    msv='22d'
                    dinner_order(q)
                    break
                if d[0]=='23d':
                    q=int(input('enter the quantity of poori:'))
                    chckquantity()
                    msv='23d'
                    dinner_order(q)
                    break
                if d[0]=='24d':
                    q=int(input('enter the quantity of chola poori:'))
                    chckquantity()
                    msv='24d'
                    dinner_order(q)
                    break
                if d[0]=='25d':
                    q=int(input('enter the quantity of dhal fry:'))
                    chckquantity()
                    msv='25d'
                    dinner_order(q)
                    break
                if d[0]=='26d':
                    q=int(input('enter the quantity of dhal palak:'))
                    chckquantity()
                    msv='26d'
                    dinner_order(q)
                    break
                if d[0]=='27d':
                    q=int(input('enter the quantity of mix veg curry:'))
                    chckquantity()
                    msv='27d'
                    dinner_order(q)
                    break
                if d[0]=='28d':
                    q=int(input('enter the quantity of panner butter masala:'))
                    chckquantity()
                    msv='28d'
                    dinner_order(q)
                    break
                if d[0]=='29d':
                    q=int(input('enter the quantity of green peas masala:'))
                    chckquantity()
                    msv='29d'
                    dinner_order(q)
                    break
                if d[0]=='30d':
                    q=int(input('enter the quantity of panner tikka masala:'))
                    chckquantity()
                    msv='30d'
                    dinner_order(q)
                    break
                if d[0]=='31d':
                    q=int(input('enter the quantity of kadai panner:'))
                    chckquantity()
                    msv='31d'
                    dinner_order(q)
                    break
                if d[0]=='32d':
                    q=int(input('enter the quantity of kadai mushroom:'))
                    chckquantity()
                    msv='32d'
                    dinner_order(q)
                    break
                if d[0]=='33d':
                    q=int(input('enter the quantity of chenna masala:'))
                    chckquantity()
                    msv='33d'
                    dinner_order(q)
                    break
                if d[0]=='34d':
                    q=int(input('enter the quantity of malai kuhfta:'))
                    chckquantity()
                    msv='34d'
                    dinner_order(q)
                    break
                if d[0]=='35d':
                    q=int(input('enter the quantity of veg kuhfta:'))
                    chckquantity()
                    msv='35d'
                    dinner_order(q)
                    break
                if d[0]=='36d':
                    q=int(input('enter the quantity of veg noodles:'))
                    chckquantity()
                    msv='36d'
                    dinner_order(q)
                    break
                if d[0]=='37d':
                    q=int(input('enter the quantity of mushroom noodles:'))
                    chckquantity()
                    msv='37d'
                    dinner_order(q)
                    break
                if d[0]=='38d':
                    q=int(input('enter the quantity of szeschwan noodles:'))
                    chckquantity()
                    msv='38d'
                    dinner_order(q)
                    break
                if d[0]=='39d':
                    q=int(input('enter the quantity of veg fried rice:'))
                    chckquantity()
                    msv='39d'
                    dinner_order(q)
                    break
                if d[0]=='40d':
                    q=int(input('enter the quantity of mushroom fried rice:'))
                    chckquantity()
                    msv='40d'
                    dinner_order(q)
                    break
                if d[0]=='41d':
                    q=int(input('enter the quantity of jeera rice:'))
                    chckquantity()
                    msv='41d'
                    dinner_order(q)
                    break
                if d[0]=='42d':
                    q=int(input('enter the quantity of veg pulav:'))
                    chckquantity()
                    msv='42d'
                    dinner_order(q)
                    break
                if d[0]=='43d':
                    q=int(input('enter the quantity of garlic fried rice:'))
                    chckquantity()
                    msv='43d'
                    dinner_order(q)
                    break
                if d[0]=='44d':
                    q=int(input('enter the quantity of szeshwan fried rice:'))
                    chckquantity()
                    msv='44d'
                    dinner_order(q)
                    break

    def bevarages():
        print('                           BEVARAGES                         ')
        print('')
        print('')
        print('                       SMOOTHIES & MOCTAILS                  ')
        print('    |',end='')
        print('-'*72)
        print('    |  FOOD NUMBER  |        FOOD NAME         |   PRICE    |')
        print('    |',end='')
        print('-'*72)
        print('    |      01bv      |   watermelon magic      |   Rs.100   |')                 
        print('    |      02bv      |   blackgrape shake      |   Rs.100   |')
        print('    |      03bv      |   summer time madness   |   Rs.100   |')
        print('    |      04bv      |   apple classic mint    |   Rs.100   |')
        print('    |      05bv      |   cucumber cooler       |   Rs.100   |')
        print('    |      06bv      |   beet the root         |   Rs.100   |')
        print('    |      07bv      |   blue mojito           |   Rs.150   |')
        print('    |      08bv      |   virgin mojito         |   Rs.150   |')
        print('    |      09bv      |   guava mojito          |   Rs.150   |')
        print('    |      10bv      |   watermelon mojito     |   Rs.150   |')
        print('    |      11bv      |   oreo shake            |   Rs.100   |')
        print('    |      12bv      |   chocolate shake       |   Rs.80    |')
        print('    |',end='')
        print('='*72)
        print('')
        print('                      VINTAGE DRINKS                 ')
        print('    |',end='')
        print('-'*72)
        print('    |  FOOD NUMBER   |   FOOD NAME      |   PRICE   |')
        print('    |',end='')
        print('-'*72)
        print('    |      13bv      |   hot coffee     |   Rs.50   |')
        print('    |      14bv      |   cold coffee    |   Rs.60   |')
        print('    |      15bv      |   black coffee   |   Rs.60   |')
        print('    |      16bv      |   hot tea        |   Rs.50   |')
        print('    |      17bv      |   green tea      |   Rs.60   |')
        print('    |      18bv      |   black tea      |   Rs.70   |')
        print('    |      19bv      |   rosemilk       |   Rs.45   |')               
        print('    |      20bv      |   badam milk     |   Rs.40   |')
        print('    |      21bv      |   butter milk    |   Rs.50   |')
        print('    |',end='')
        print('='*72)
        
        def bevarages_order(qbv):
            chckp='select price from bevarages where foodid=%s'
            ms=(msv,)
            cur.execute(chckp,ms)
            fetch_price=cur.fetchone()
            fpint=int(fetch_price[0])
            p=fpint*qbv
            global bill
            bill+=p

        def chckquantity():
            if str(q) in 'abcdefghijklamnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVW!@#$%^&*()_+=-}{][;:><.,?/|':
                print('enter the valid quantity:')

        #BEVARAGES_MAIN
        itmnos5=input('enter the food numbers to order: ')
        global foodid
        foodid+=itmnos5
        item=itmnos5.split(',')
        cur.execute('select foodid from bevarages')
        f1=cur.fetchall()
        for bv in f1:          
            while bv[0] in item:
                if bv[0]=='01bv':
                    q=int(input('enter the quantity of watermelon magic:'))
                    chckquantity()
                    msv='01bv'
                    bevarages_order(q)
                    break
                if bv[0]=='02bv':
                    q=int(input('enter the quantity of blackgrape shake:'))
                    chckquantity()
                    msv='02bv'
                    bevarages_order(q)
                    break
                if bv[0]=='03bv':
                    q=int(input('enter the quantity of summer time maddness:'))
                    chckquantity()
                    msv='03bv'
                    bevarages_order(q)
                    break
                if bv[0]=='04bv':
                    q=int(input('enter the quantity of apple classic mint:'))
                    chckquantity()
                    msv='04bv'
                    bevarages_order(q)
                    break
                if bv[0]=='05bv':
                    q=int(input('enter the quantity of cucumber cooler:'))
                    chckquantity()
                    msv='05bv'
                    bevarages_order(q)
                    break
                if bv[0]=='06bv':
                    q=int(input('enter the quantity of beet the root:'))
                    chckquantity()
                    msv='06bv'
                    bevarages_order(q)
                    break
                if bv[0]=='07bv':
                    q=int(input('enter the quantity of blue mojito:'))
                    chckquantity()
                    msv='07bv'
                    bevarages_order(q)
                    break
                if bv[0]=='08bv':
                    q=int(input('enter the quantity of virgin mojito:'))
                    chckquantity()
                    msv='08bv'
                    bevarages_order(q)
                    break
                if bv[0]=='09bv':
                    q=int(input('enter the quantity of guava mojito:'))
                    chckquantity()
                    msv='09bv'
                    bevarages_order(q)
                    break
                if bv[0]=='10bv':
                    q=int(input('enter the quantity of watermelon mojito:'))
                    chckquantity()
                    msv='10bv'
                    bevarages_order(q)
                    break
                if bv[0]=='11bv':
                    q=int(input('enter the quantity of oreo shake:'))
                    chckquantity()
                    msv='11bv'
                    bevarages_order(q)
                    break
                if bv[0]=='12bv':
                    q=int(input('enter the quantity of chocolate shake:'))
                    chckquantity()
                    msv='12bv'
                    bevarages_order(q)
                    break
                if bv[0]=='13bv':
                    q=int(input('enter the quantity of hot coffee:'))
                    chckquantity()
                    msv='13bv'
                    bevarages_order(q)
                    break
                if bv[0]=='14bv':
                    q=int(input('enter the quantity of cold coffee:'))
                    chckquantity()
                    msv='14bv'
                    bevarages_order(q)
                    break
                if bv[0]=='15bv':
                    q=int(input('enter the quantity of black coffee:'))
                    chckquantity()
                    msv='15bv'
                    bevarages_order(q)
                    break
                if bv[0]=='16bv':
                    q=int(input('enter the quantity of hot tea:'))
                    chckquantity()
                    msv='16bv'
                    bevarages_order(q)
                    break
                if bv[0]=='17bv':
                    q=int(input('enter the quantity of green tea:'))
                    chckquantity()
                    msv='17bv'
                    bevarages_order(q)
                    break
                if bv[0]=='18bv':
                    q=int(input('enter the quantity of black tea:'))
                    chckquantity()
                    msv='18bv'
                    bevarages_order(q)
                    break
                if bv[0]=='19bv':
                    q=int(input('enter the quantity of rose milk:'))
                    chckquantity()
                    msv='19bv'
                    bevarages_order(q)
                    break
                if bv[0]=='20bv':
                    q=int(input('enter the quantity of badam milk:'))
                    chckquantity()
                    msv='20bv'
                    bevarages_order(q)
                    break
                if bv[0]=='21bv':
                    q=int(input('enter the quantity of butter milk:'))
                    chckquantity()
                    msv='21bv'
                    bevarages_order(q)
                    break
    
    def desserts():
        print('')
        print('                           DESSERTS                     ')
        print('')
        print('')
        print('                               CAKES                  ')
        print('    |',end='')
        print('-'*72)
        print('    |  FOOD NUMBER  |        FOOD NAME          |   PRICE    |')
        print('    |',end='')
        print('-'*72)
        print('    |      01dt      |   tiramisu               |   Rs.100   |')                 
        print('    |      02dt      |   cheese cake            |   Rs.60    |')
        print('    |      03dt      |   red velvet cake        |   Rs.65    |')
        print('    |      04dt      |   rainbow cake           |   Rs.90    |')
        print('    |      05dt      |   blackforest cake       |   Rs.70    |')
        print('    |      06dt      |   hot Choco fudge cake   |   Rs.110   |')
        print('    |      07dt      |   Cup cake               |   Rs.40    |')
        print('')
        print('')
        print('                             BROWNIE                  ')
        print('    |',end='')
        print('-'*72)
        print('    |  FOOD NUMBER  |        FOOD NAME            |   PRICE    |')
        print('    |',end='')
        print('-'*72)
        print('    |      08dt      |   Brownie with ice cream   |   Rs.110   |')
        print('    |      09dt      |   hazelnut Brownie         |   Rs.130   |')
        print('    |      10dt      |   Hot sizzling Brownie     |   Rs.125   |')
        print('')
        print('')
        print('                             ICE CREAM                  ')
        print('    |',end='')
        print('-'*72)
        print('    |  FOOD NUMBER  |        FOOD NAME        |   PRICE    |')
        print('    |',end='')
        print('    |      11dt      |   death-by-chocolate   |   Rs.300   |')
        print('    |      12dt      |   Butterscotch cone    |   Rs.75    |')
        print('    |      13dt      |   Chocolate cone       |   Rs.75   |')
        print('    |      14dt      |   Blackcurrant cone    |   Rs.75   |')
        print('    |      15dt      |   Kulfi                |   Rs.65   |')
        print('')
        print('                             WAFFLE                  ')
        print('    |',end='')
        print('-'*72)
        print('    |  FOOD NUMBER  |        FOOD NAME           |   PRICE    |')
        print('    |',end='')
        print('    |      16dt      |   Waffle with ice cream   |   Rs.110   |')
        print('    |      17dt      |   belgium waffle          |   Rs.200   |')
        print('    |      18dt      |   waffle pan cakes        |   Rs.150   |')
        print('')
        print('                             SAVOURY                  ')
        print('    |',end='')
        print('-'*72)
        print('    |  FOOD NUMBER  |        FOOD NAME         |   PRICE    |')
        print('    |',end='')
        print('    |      19dt      |   gulab jamun   |   Rs.30   |')               
        print('    |      20dt      |   rasamalai     |   Rs.30   |')
        print('    |      21dt      |   jalebi        |   Rs.25   |')
        print('    |',end='')
        print('='*72)    

        def desserts_order(qdt):
            chckp='select price from desserts where foodid=%s'
            ms=(msv,)
            cur.execute(chckp,ms)
            fetch_price=cur.fetchone()
            fpint=int(fetch_price[0])
            p=fpint*qdt
            global bill
            bill+=p

        def chckquantity():
            if str(q) in 'abcdefghijklamnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVW!@#$%^&*()_+=-}{][;:><.,?/|':
                print('enter the valid quantity:')

        #DESSERTS_MAIN
        itmnos6=input('enter the food numbers to order: ')
        global foodid
        foodid+=itmnos6
        item=itmnos6.split(',')
        cur.execute('select foodid from desserts')
        f1=cur.fetchall()
        for dt in f1:          
            while dt[0] in item:
                if dt[0]=='01dt':
                    q=int(input('enter the quantity of Tiramisu:'))
                    chckquantity()
                    msv='01dt'
                    desserts_order(q)
                    break
                if dt[0]=='02dt':
                    q=int(input('enter the quantity of Cheese cake:'))
                    chckquantity()
                    msv='02dt'
                    desserts_order(q)
                    break
                if dt[0]=='03dt':
                    q=int(input('enter the quantity of Red velvet cake:'))
                    chckquantity()
                    msv='03dt'
                    desserts_order(q)
                    break
                if dt[0]=='04dt':
                    q=int(input('enter the quantity of rainbow cake:'))
                    chckquantity()
                    msv='04dt'
                    desserts_order(q)
                    break
                if dt[0]=='05dt':
                    q=int(input('enter the quantity of blackforest cake:'))
                    chckquantity()
                    msv='05dt'
                    desserts_order(q)
                    break
                if dt[0]=='06dt':
                    q=int(input('enter the quantity of hot Choco fudge cake:'))
                    chckquantity()
                    msv='06dt'
                    desserts_order(q)
                    break
                if dt[0]=='07dt':
                    q=int(input('enter the quantity of Cup cake:'))
                    chckquantity()
                    msv='07dt'
                    desserts_order(q)
                    break
                if dt[0]=='08dt':
                    q=int(input('enter the quantity of Brownie with ice cream:'))
                    chckquantity()
                    msv='08dt'
                    desserts_order(q)
                    break
                if dt[0]=='09dt':
                    q=int(input('enter the quantity of hazelnut Brownie:'))
                    chckquantity()
                    msv='09dt'
                    desserts_order(q)
                    break
                if dt[0]=='10dt':
                    q=int(input('enter the quantity of Hot sizzling Brownie:'))
                    chckquantity()
                    msv='10dt'
                    desserts_order(q)
                    break
                if dt[0]=='11dt':
                    q=int(input('enter the quantity of death-by-chocolate:'))
                    chckquantity()
                    msv='11dt'
                    desserts_order(q)
                    break
                if dt[0]=='12dt':
                    q=int(input('enter the quantity of Butterscotch cone:'))
                    chckquantity()
                    msv='12dt'
                    desserts_order(q)
                    break
                if dt[0]=='13dt':
                    q=int(input('enter the quantity of Chocolate cone:'))
                    chckquantity()
                    msv='13dt'
                    desserts_order(q)
                    break
                if dt[0]=='14dt':
                    q=int(input('enter the quantity of Blackcurrant cone:'))
                    chckquantity()
                    msv='14dt'
                    desserts_order(q)
                    break
                if dt[0]=='15dt':
                    q=int(input('enter the quantity of Kulfi:'))
                    chckquantity()
                    msv='15dt'
                    desserts_order(q)
                    break
                if dt[0]=='16dt':
                    q=int(input('enter the quantity of Waffle with ice cream:'))
                    chckquantity()
                    msv='16dt'
                    desserts_order(q)
                    break
                if dt[0]=='17dt':
                    q=int(input('enter the quantity of belgium waffle:'))
                    chckquantity()
                    msv='17dt'
                    desserts_order(q)
                    break
                if dt[0]=='18dt':
                    q=int(input('enter the quantity of waffle pan cakes:'))
                    chckquantity()
                    msv='18dt'
                    desserts_order(q)
                    break
                if dt[0]=='19dt':
                    q=int(input('enter the quantity of gulab jamun:'))
                    chckquantity()
                    msv='19dt'
                    desserts_order(q)
                    break
                if dt[0]=='20dt':
                    q=int(input('enter the quantity of rasamalai:'))
                    chckquantity()
                    msv='20dt'
                    desserts_order(q)
                    break
                if dt[0]=='21dt':
                    q=int(input('enter the quantity of jalebi:'))
                    chckquantity()
                    msv='21dt'
                    desserts_order(q)
                    break
            





    #ORDER_MAIN
    while True:
        order_menu()
        o=int(input('enter your choice:'))
        if o==1:
            starters()
            order_cntnu()
            oc=input('enter your choice:')
            if oc in 'Nn':
                break            
        elif o==2:
            breakfast()
            order_cntnu()
            oc=input('enter your choice:')
            if oc in 'Nn':
                break
        elif o==3:
            lunch()
            order_cntnu()
            oc=input('enter your choice:')
            if oc in 'Nn':
                break
        elif o==4:
            dinner()
            order_cntnu()
            oc=input('enter your choice:')
            if oc in 'Nn':
                break
        elif o==5:
            bevarages()
            order_cntnu()
            oc=input('enter your choice:')
            if oc in 'Nn':
                break
        elif o==6:
            desserts()
            order_cntnu()
            oc=input('enter your choice:')
            if oc in 'Nn':
                break


#MAIN CODE
import mysql.connector
con=mysql.connector.connect(host='localhost',user='root',passwd='Tvsahosur$123',database='online_food_order')
if con.is_connected():
    print(' W E L C O M E    T O    O N L I N E    F O O D    O R D E R I N G    S Y S T E M ')
    
cur=con.cursor()

while True:
    welcome()
    c=int(input('enter your choice: '))
    if c==1:
        print('*'*80)
        print('TO CREATE AN ACCOUNT FILL THE FOLLOWING DETAILS')
        print('*'*80)
        custname=input('enter your name: ')
        phno=phnumber_validity()
        email=email_validity()
        address=input('enter your address: ')
        password=passwd_validity()
        cust_details='insert into customer_details (custname,phno,email,address,password)values(%s,%s,%s,%s,%s)'
        values=(custname,phno,email,address,password)
        cur.execute(cust_details,values)
        con.commit()
        customer_id='select custid from customer_details where email=%s'
        mail=(email,)
        cur.execute(customer_id,mail)
        p=cur.fetchone()
        p=p[0]
        print('YOUR CUSTOMER_ID IS: ',p)
        print('')
        print('THANK YOU FOR CREATING AN ACCOUNT')
    elif c==2:
        print('FILL THE FOLLOWING DETAILS TO LOGIN TO YOUR ACCOUNT')
        custid=int(input('enter your customer id:'))
        custname=input('enter your name:')
        password=input('enter your password[4 CHARACTERS]:')
        cur.execute('select * from customer_details')
        f=cur.fetchall()
        for i in f:
            if (custid in i) and (custname in i) and (password in i):
                print('LOGIN SUCCESSFUL')
                login()
                l=int(input('enter your choice: '))
                if l==1:
                    print('YOUR INFO:')
                    see='select * from customer_details where custid=%s'
                    mods=(custid,)
                    cur.execute(see,mods)
                    p=cur.fetchall()
                    print('YOUR DETAILS ARE')
                    for i in p:
                        print(i)
                elif l==2:
                    yid=input('enter your id:')
                    login_update()
                    u=int(input('enter your choice: '))
                    if u==1:
                        ut=input('change the name to: ')
                        upd='update customer_details set custname=%s where custid=%s'
                        mods=(ut,yid)
                        cur.execute(upd,mods)
                        con.commit()
                    elif u==2:
                        ut=int(input('change the phone number to: '))
                        upd='update customer_details set phno=%s where custid=%s'
                        mods=(ut,yid)
                        cur.execute(upd,mods)
                        con.commit()
                    elif u==3:
                        ut=input('chenge the email to: ')
                        upd='update customer_details set email=%s where custid=%s'
                        mods=(ut,yid)
                        cur.execute(upd,mods)
                        con.commit()
                    elif u==4:
                        ut=input('update the address to: ')
                        upd='update customer_details set address=%s where custid=%s'
                        mods=(ut,yid)
                        cur.execute(upd,mods)
                        con.commit()
                    elif u==5:
                        ut=input('update the password to: ')
                        upd='update customer_details set password=%s where custid=%s'
                        mods=(ut,yid)
                        cur.execute(upd,mods)
                        con.commit()

                elif l==3:
                    while True:
                        bill=0
                        foodid=''                        
                        order()
                        order_meth()
                        oi=input('Enter your choice: ')
                        if oi in 'Tt':
                            adupdate='select address from customer_details where custid=%s'
                            adupdatev=(custid,)
                            cur.execute(adupdate,adupdatev)
                            upsalfetch=cur.fetchone()
                            adrs=upsalfetch[0]
                            insert='insert into sales(custid,custname,foodids,bill,address) values(%s,%s,%s,%s,%s)'
                            values=(custid,custname,foodid,bill,adrs)
                            cur.execute(insert,values)
                            con.commit()
                            print('ORDERED SUCCESSFULLY')
                        elif oi in 'Ss':
                            aentadrs='select address from customer_details where custid=%s'
                            aentv=(custid,)
                            cur.execute(aentadrs,aentv)
                            upsalfetch=cur.fetchone()
                            adrs=upsalfetch[0]
                            insert='insert into sales(custid,custname,foodids,bill,address) values(%s,%s,%s,%s,%s)'
                            values=(custid,custname,foodid,bill,adrs)
                            cur.execute(insert,values)
                            con.commit()
                            print('ORDERED SUCCESSFULLY')
                        elif oi in 'Dd':
                            adrs=input('enter the location to deliever the food: ')
                            insert='insert into sales(custid,custname,foodids,bill,address) values(%s,%s,%s,%s,%s)'
                            values=(custid,custname,foodid,bill,adrs)
                            cur.execute(insert,values)
                            con.commit()
                            print('ORDERED SUCCESSFULLY')
            else:
                print('YOU DONT HAVE AN ACCOUNT, CREATE A NEW ACCOUNT AND LOGIN AGAIN..')
    else:
        print('enter valid choice!')
        continue                        
                    
                        