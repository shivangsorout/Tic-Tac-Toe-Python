game = [[0,0,0],
        [0,0,0],
        [0,0,0],]


def game_board():                       #this is how we define a function in python3
    print('   a  b  c')                 #the spaces before the line is the starting of the block
    for count, row in enumerate(game):  #we don't use the brackets({}) in python. The blocks are shown using spaces
        print(count, row)

game_board()                            #this is how we call a funtion in python
x = game_board                          #function without parenthesis is just pointing at that funtion but not calling itself

game[0][2] = 1

x()                                     #we assign a variable a function  