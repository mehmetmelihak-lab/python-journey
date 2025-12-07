import random

def password_generator():
    length = int(input('Please enter the length of your desired password: '))

    capital = input('Do you want upper case letters? yes or no: ').lower()
    miniscule = input('Do you want lower case letters? yes or no: ').lower()
    number = input('Do you want numbers? yes or no: ').lower()
    special_letter = input('Do you want special letters? yes or no: ').lower()

    pool = ""

    if capital == 'yes':
        pool += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if miniscule == 'yes':
        pool += 'abcdefghijklmnopqrstuvwxyz'
    if number == 'yes':
        pool += '0123456789'
    if special_letter == 'yes':
        pool += '!@#$%^&*()_-+='

    if pool == "":
        print("Error: You must select at least one character type.")
        return

    password = "".join(random.choices(pool, k=length))
    print(f'Generated password = {password}')

    
        
        



