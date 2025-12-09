import random

def dice_roller():
    while True:
        while True:
            try:
                amount = int(input('How many dices do you want to roll?: '))
                if amount <= 0:
                    print('Please enter a positive number')
                    continue
                break
            except ValueError:
                print('Please enter an integer')
        
        
        roll_list = []
        for roll in range(amount):
            result = random.randint(1, 6)
            roll_list.append(result)
        
        print(f'Your list is {roll_list} and you have rolled {amount} times')

        
        while True:
            again = input('Do you want to roll again? (yes/no): ')
            if again.lower() == 'yes':
                break
            elif again.lower() == 'no':
                print('Quitting the dice roller')
                return
            else:
                print('Please only type yes or no')

dice_roller()
        
        