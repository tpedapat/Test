from math import rand
import random


def disp_board(game):
    print(game[0]+'|'+game[1]+'|'+game[2])
    print(game[3] + '|' + game[4] + '|' + game[5])
    print(game[6] + '|' + game[7] + '|' + game[8])


print(random.randint(1,50))

def Toss():
    Name=input('enter your name: ')
    decision=input('{}, you want to go with heads(H) or tails(T)'.format(Name))
    toss_no=random.randint(1,50)
    if(toss_no%2 == 0 ):
        toss = 'H'
    else:
        toss = 'T'
    if(decision == toss):
        symb=input('{} u have won toss..which symbol u want to take o or x ?'.format(Name))
        won = 1
        if(symb == 'o'):
            symb_2 = 'x'
        else:
            symb_2 = 'o'

        print('{} your symbol is {} '.format(Name,symb))
        print('second player symbol is {} '.format( symb_2))
    else:
        won = 2
        print('{} you lost the toss'.format(Name))
        symb_2 = input('player 2 have won toss..which symbol u want to take o or x ?')
        if (symb_2 == 'o'):
            symb = 'x'
        else:
            symb = 'o'
        print('second player symbol is {} '.format(symb_2))
        print('{} your symbol is {} '.format(Name, symb))
    return (symb,symb_2,won)

def update_board(board,pos,symbol):
    if (board[pos] == ' '):
        board[pos] = symbol
        return True
    else:
        return False

def wincheck(board,mark):
        return ((board[6] == mark and board[7] == mark and board[8] == mark) or  # across the top
        (board[3] == mark and board[4] == mark and board[5] == mark) or  # across the middle
        (board[0] == mark and board[1] == mark and board[2] == mark) or  # across the bottom
        (board[6] == mark and board[3] == mark and board[0] == mark) or  # down the middle
        (board[7] == mark and board[4] == mark and board[1] == mark) or  # down the middle
        (board[8] == mark and board[5] == mark and board[2] == mark) or  # down the right side
        (board[6] == mark and board[4] == mark and board[2] == mark) or  # diagonal
        (board[8] == mark and board[4] == mark and board[0] == mark))  # diagonal


while(True):
    board = [' '] * 9
    game_on = True
    (a,b,won_)=Toss()
    if(won_==1):
        Turn_v = input('Teja, you wanna play first(F) or second(S)?')
        if(Turn_v == 'F'):
            Turn=True
        else:
            Turn = False
    else:
        Turn_v = input('2nd player, you wanna play first(F) or second(S)?')
        if (Turn_v == 'F'):
            Turn = False
        else:
            Turn = True


    while(game_on):
        if (Turn == True):
            position=int(input('Teja, where u want to place ?'))
            pos_check=update_board(board,position,a)
            if(pos_check == True):
                disp_board(board)
                bool = wincheck(board,a)
                if(bool == True):
                    print('player 1 wins')
                    game_on = False
                    play_again =input('do u want to play another round y or n ?')
                    if(play_again == 'n'):
                        replay = False
                    else:
                        replay = True

                else:
                    Turn = False
            else:
                print('Choose another position please')
        else:
            position = int(input('2nd player, where u want to place ?'))
            pos_check =update_board(board, position, b)
            if (pos_check == True):
                disp_board(board)
                bool = wincheck(board, b)
                if (bool == True):
                    print('player 2 wins')
                    game_on = False
                    play_again = input('do u want to play another round y or n ?')
                    if (play_again == 'n'):
                        replay = False
                    else:
                        replay = True
                else:
                    Turn = True
            else:
                print('Choose another position please')

    if(replay == False):
        break
    else:
        continue















