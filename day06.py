def say_hello():
    print('Hello')
say_hello()
def is_even(number):
    if number%2==0:
        return True
    else:
        return False
def isevenbutbetter(number):
    return number%2==0
is_even(2)
isevenbutbetter(2)
def calculate_area(length,width):
    area=length * width
    print(f"{length}x{width}={area}")
    return area
length1=float(input('Please enter the length of our object:'))
width1=float(input('Please enter the width of our object:'))
calculate_area(length1,width1)
def find_largest(a,b,c):
    if a>=b and a>=c:
        print(f'{a} is the largest')
    elif b>=a and b>=c:
        print(f'{b} is the largest')
    elif c>=a and c>=b:
        print(f'{c} is the largest')
    else:
        print('All numbers are equal')
find_largest(1,2,3)
def factorial(n):
    result=1
    for i in range(1,n+1):
        result*=i
    return result
print(factorial(5))
n=10
f=1
for i in range(1,n+1):
    f*=i
print(f)
def count_vowels2(text):
    count=0
    vowels='aeiouAEIOU'
    for char in text:
        if char in vowels:
            count+=1
    return count
count_vowels2('Melih')