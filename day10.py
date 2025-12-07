import random
def password_generator():
    length=int(input('Please enter the length of your desired password:'))
    capital=input('Do you want upper case letters  ? yes or no please:').lower()
    miniscule=input('Do you want lower case letters ? yes or no please:').lower()
    number=input('Do you want numbers ? yes or no please:').lower()
    special_letter=input('Do you want special letters ? yes or no please:').lower()
    pool=""
    if capital=='yes':
        pool+='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if miniscule=='yes':
        pool+='abcdefghijklmnopqrstuvwxyz'
    if number=='yes':
        pool+='1234567890'
    if special_letter=='yes':
        pool+='!@#$%^&*()_-+='
    if pool=="":
        print('There is an error try again')
        return
    
    password="".join(random.choices(pool,k=length))
    print(f'Generated password={password}')

    
        
        



