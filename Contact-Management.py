#-------------Contact Book Management-------------
#-------------Create Contact----------------------
def create():
    while 1:
        print("-------------Create Contact----------------------")
        name=input("Enter Name or press 0 for exit:").lower()
        if name=='0':
            break
        if name not in d:
            mob=input("Enter Mobile Number or press 0 for exit:")
            if mob=='0':
                break
            if mob not in list(d.values()):
                d.update({name:mob})
                print("Successfully added new contact")
                break
            else:
                print('''This Mobile Number already exists''')
                print("With this Name:",list(d.keys())[list(d.values()).index(mob)])
                c=input('''Press for
(1)Update Contact
(2)Exit
''')
                if c=="1":
                    update()
                else:
                    pass
        else:
            print('''Contact already exists''')
        
        
#--------------Search Contact------------------------
def read():
    print("--------------Search Contact------------------------")
    r=input("Enter Contact Name or Contact Number:")
    if r.isdigit():
        if r in list(d.values()):
            n= list(d.keys())[list(d.values()).index(r)]
            print("Contact Name:",n)
            print("Contact Numer:",r)
            return n
        else:
            print("Number not in Contact.")
            return 0
    else:
        if r in d:
            print(r)
            print(d[r])
            return r
        else:
            print('''Contact doesn't Exists''')
            return 0
        
#-------------Update Contact------------------------
def update():
    print("-------------Update Contact------------------------")
    v=read()
    if v==0:
        return
    else:
        n=input("Enter new Contact Name or Contact Numer:")
        if n.isdigit():
            d[v]=n
            print("Contact Updated Sucessfully")
        else:
            x=d.pop(v)
            print(x)
            d.update({n:x})
            print("Contact Updated Sucessfully")
#-------------Delete Contact------------------------
def delete():
    print("-------------Delete Contact------------------------") 
    v=read()
    if v==0:
        return
    else:
        d.pop(v)
        print("Deleted Sucessfully")
#--------------Main Code---------------------------
print("-------------Welcome Contact Book Management -------------")
d={}
while 1:
    b=(input('''Choose one option
    (1) New Contact
    (2) Search Contact 
    (3) Update Contact
    (4) Delete Contact
    (5) Exit
    '''))
    if b=="1":
        create()
    elif b=="2":
         read()
    elif b=="3":
        update()
    elif b=="4":
        delete()
    elif b=="5":
        break
    else:
        print('''You Choose Incorrect Option
        Please Choose Correct One''')
