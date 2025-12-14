birthdays= {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

while True:
    name=input('Enter a name: (blank to quit): ')
    if name=='':
        break
    elif name in birthdays:
        print(f"{name}'s birthday is:{birthdays[name]}")
    else:
        bday=input("This person is not in the program.I could add him/her.If you want me to do that enter their birthday if not just leave blank: ")
        if bday=='':
            break
        else:
            birthdays[name]=bday


