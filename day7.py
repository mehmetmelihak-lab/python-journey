me={
    'name':'Melih',
    'age':'19',
    'City':'Istanbul',
    'Hobby':'Playing the guitar'
}
print(me)
countries_and_capitals={
    'Turkiye':'Ankara',
    'Canada':'Ottawa',
    'United States':'Washington,DC',
    'Belgium':'Brussels',
    'Netherlands':'Amsterdam'
}
user_country=input('Please enter the country you want to know the capital of:')
if user_country not in countries_and_capitals:
    print('Not found')
else:
    print(f'The capital is:{countries_and_capitals[user_country]}')
students_and_grades={
    'Melih':90,
    'John':50,
    'Sadık':60
}
maximum_grade=max(students_and_grades.values())
print(maximum_grade)
count={}
sentence = input("Enter a sentence: ")
count = {}
for word in sentence.split():
    count[word] = count.get(word, 0) + 1

for word, frequency in count.items():
    print(f"{word}: {frequency}")

students={
    'Ahmet':{'name':'Ahmet',
         'age':19,
         'grades':[90,20,80]
    },
    'Melih':{       'name':'Melih',
        'age':19,
        'grades':[0,10,40]
     

    },
    'Nazim':{
     

        'name':'Nazim',
        'age':18,
        'grades':[100,20,100]
    }
         
         
}
for student_id,info in students.items():
    name=info['name']
    age=info['age']
    grades=info['grades']
    average=sum(grades)/len(grades)
    print(f'{name} {student_id}')
    print(f'age:{age}')
    print(f'grades:{grades}')
    print(f'end grade:{average:.1f}')
