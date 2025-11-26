#Day 3:If else conditions:
age=19
if age>=18:
    print('You are an adult')
else:
    print('you are a minor')
score=int(input('Please enter your score:'))
if score>=90:
    print('Grade A')
elif score>=80:
    print('Grade B')
elif score>=70:
    print('Grade c')
elif score>=60:
    print('Grade D')
else:
    print('Grade F')
#Logical operators:
temperature = int(input('Please enter the Celsius of today: '))
is_sunny = input('Is it sunny today? (yes/no): ').lower() == 'yes'

if is_sunny and temperature >= 25:
      print('We have the perfect weather today')
elif is_sunny and temperature < 25:
     print('Its sunny but cold today')
elif not is_sunny and temperature < 25:
     print('Its neither sunny nor hot today')
else:
      print('Its not sunny but hot today')
gender=input('What is your gender ? M/F:')
your_gender=gender.lower()
if your_gender=='m':
            print('Hello there man.')
elif gender=='f':
            print('Hello there lady.')
else:
            print('Hello there friendoo')