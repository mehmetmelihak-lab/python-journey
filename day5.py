shopping_list = []
shopping_list.append('Fruits')
shopping_list.append('Rice')
shopping_list.append('Chicken')
print(shopping_list)
len(shopping_list)
numbers=[1,2,3,4,5]
print(numbers[0])
print(numbers[4])
print(numbers[1:4])
numbers.pop(4)
print(numbers)
numbers.remove(1)
print(numbers)
print(shopping_list)
item_number=1
index_number=0
while item_number<4:
    print(f'Item {item_number}: {shopping_list[index_number]} ')
    item_number+=1
    index_number+=1
shopping_list2 = ["apples", "milk", "bread"]

item_number = 1
index_number = 0

for item in shopping_list2:
    print(f"Item {item_number}: {shopping_list2[index_number]}")
    item_number += 1
    index_number += 1
for number in range(1,21):
    if number%3==0:
        print(number)