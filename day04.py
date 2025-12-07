# Day 4 - Loops
for i in range(1,11):
    print(i)
fruits=['Apple','Banana','Cherry','Strawberry']
for fruit in fruits:
    print(f'I love {fruit}')
count=0
while count<5:
    print(f"Count is {count}")
    count+=1
for num in range(1,20):
    if num==10:
        break # count till 10
    print(num)
for num in range(1,20):
    if num==10: 
        continue # skip 10
    print(num) 
for num in range(1,21):
    if num%2==0:
        print(num)