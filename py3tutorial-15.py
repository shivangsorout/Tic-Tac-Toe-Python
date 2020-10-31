
import itertools
from colorama import Fore, Back, Style, init

init()

def win(current_map):

    def all_same(l,pos):
        if l.count(l[0]) == len(l) and l[0] != 0:           #only one line of code
            print(f'Player {l[0]} is the winner {pos}!')
            return True
        else:
            return False

    # Horizontal
    for row in current_map:
        if all_same(row,'horizontally (-)'):
            return True

    # Vertical
    for col in range(len(current_map)):
        check = []
        for row in current_map:
            check.append(row[col])
        if all_same(check,'vertically (-)'):
            return True

    # Diagonal
    diags = []
    for idx in range(len(current_map)):
        diags.append(current_map[idx][idx])
    if all_same(diags,'diagonally (\\)'):                   # backslash(\) is usually used for escaping the value and prefixing the special 
        return True                                         # with '\' changes the character into ordinary character

    diags = []
    for row, col in enumerate(list(reversed(range(len(current_map))))):
        diags.append(game[row][col])

    if all_same(diags,'diagonally (/)'):
        return True

    return False

def game_board(game_map, player = 0, row = 0, column = 0, just_display = False):
    try:
        if game_map[row][column] != 0:
            print("This position is occupied! Please enter another position!!")
            #return False                                   #this can change the game_map from list type to bool type
            return game_map, False                          #so that is why we are using this

        if not just_display:
            game_map[row][column] = player
        print("   "+"  ".join(str(i) for i in range(game_size)))
        for count, row in enumerate(game_map):
            colored_row = ''
            for item in row:
                if item == 0:
                    colored_row += "   "
                elif item == 1:
                    colored_row += Fore.RED + " X " + Style.RESET_ALL
                elif item == 2:
                    colored_row += Fore.GREEN + " 0 " + Style.RESET_ALL
            print(count, colored_row)


        print('\n')
        return game_map, True

    except IndexError as e:
        print('Error: Make sure you input row/column as 0,1 & 2;', e)
        return game_map, False
    except Exception as e:
        print('Something is very very wrong!! ',e)
        return game_map, False

play = True
players = itertools.cycle([1,2])
while play:
    game_size = int(input('What size of game do you want to play?: '))
    game = [[0 for i in range(game_size)] for i in range(game_size)]
    game_won = False
    game,_ = game_board(game,just_display = True)           # underscore(_) means that we doesn't care about the other value the fuction is returning 
    while not game_won:
        
        current_player = next(players)
        print('Current Player:',current_player)
        played = False

        while not played:
            column_choice = int(input('What column do you want to play (0,1,2): '))
            row_choice = int(input('What row do you want to play (0,1,2): '))
            game, played = game_board(game, current_player, row_choice, column_choice)

        if win(game):
            game_won = True
            again = input('Do you wish to play again (y/n): ')

            if again.lower() == 'y':
                print('restarting...')
            elif again.lower() == 'n':
                print('Byeeeee')
                play = False
            else:
                print('Entered invalid character!!')
                play = False

