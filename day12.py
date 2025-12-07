import random
def guess_random():
    while True:
        random_guess=random.randint(1,100)
        attempts=0
        print(' Im thinking of a number between 1-100')
        while True:
            try:
                guess=int(input('Please enter your guess'))
                if guess<1 or guess>100:
                    print('please enter a number between 1 and a 100')
                elif guess>random_guess:
                    print('Thats higher than the number')
                    attempts+=1
                elif guess<random_guess:
                    print('Thats lower than the number')
                    attempts+=1
                else:
                    attempts+=1
                    print(f'You found it in {attempts} good job!')
                    break
            except ValueError:
                print('Invalid input please enter a number')
        quit_game = input('\nDo you want to play again? (yes/no): ')
        if quit_game.lower() != 'yes':
            print('Thanks for playing!')
            break
            
        
