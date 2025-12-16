The_Board={'TOP L':' ','TOP M':' ','TOP R':' ',
           'MID L':' ','MID M':' ','MID R':' ',
           'BOT L':' ','BOT M':' ','BOT R':' '


}
def board_maxx(board):
    print(board['TOP L']+'|'+board['TOP M']+'|'+board['TOP R'])
    print(board['MID L']+'|'+board['MID M']+'|'+board['MID R'])
    print(board['BOT L']+'|'+board['BOT M']+'|'+board['BOT R'])

def inpt():
    while True:
        player1=input('Please enter your choice: X/O: ')
        if player1.upper()=='X':
            return 'X','O'
        elif player1.upper()=='O':
            return 'O','X'
        else:
            print('Only X or O please.')
player1,player2=inpt()
print(f'Player 1 is:{player1} and Player 2 is:{player2}')

def make_move(board,player):
    while True:

        position=input(f'Please choose a position for {player} (TOP L/M/R, MID L/M/R, BOT L/M/R): ')
        if position.upper() in board and board[position.upper()]==' ':
            board[position.upper()]=player
            board_maxx(board)
            break
        
        else:
            print('INVALID MOVE,TRY AGAIN')

    



def check_winner(board, player):
    if board['BOT L'] == board['BOT M'] == board['BOT R'] == player:
        return True
    if board['MID L'] == board['MID M'] == board['MID R'] == player:
        return True
    if board['TOP L'] == board['TOP M'] == board['TOP R'] == player:
        return True
    
    if board['TOP L'] == board['MID L'] == board['BOT L'] == player:
        return True
    if board['TOP M'] == board['MID M'] == board['BOT M'] == player:
        return True
    if board['TOP R'] == board['MID R'] == board['BOT R'] == player:
        return True
    
    if board['TOP L'] == board['MID M'] == board['BOT R'] == player:
        return True
    if board['TOP R'] == board['MID M'] == board['BOT L'] == player:
        return True
    return False
def reset(board):
    for key in board.keys():
        board[key]=' '
def is_draw(board):
    return ' ' not in board.values()


while True:
    make_move(The_Board,player1)
    if check_winner(The_Board,player1)==True:
        game_over=input('The winner is Player 1! Do you want to play again ? Y/N')
        if game_over.upper()=='Y':
            reset(The_Board)
            continue
        else:
            break
    make_move(The_Board,player2)
    if check_winner(The_Board,player2)==True:
        game_over=input('The winner is Player 2! Do you want to play again ? Y/N: ')
        if game_over.upper()=='Y':
            reset(The_Board)
            continue

        else:
            break
    if is_draw(The_Board):
        game_over = input("It's a draw! Do you want to play again? Y/N: ")
        if game_over.upper() == 'Y':
            reset(The_Board)
            continue
        else:
            break



    

