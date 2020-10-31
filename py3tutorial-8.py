
'''
game = "I want to play valorant"
print(id(game))     #--(1)

def game_board(player=0,row=0,column=0,just_player = False):
    game = "valorant"
    print(id(game)) #--(2)
    print(game)     

game_board()
print(id(game))     #--(3)
print(game)         #because strings are immutable so that is why id (1) and (3) are same and id (2) is different
'''


'''
game = [1,2,3]
print(id(game))         #--(1)

def game_board():
    game[1] = "a"       #for this the value of all the id's are same
    #game = "a"         #but for this the value of id (1) and (3) are same
    print(game)
    print(id(game))     #--(2)

game_board()
print(game)
print(id(game))         #--(3)
'''


'''
game = "I am going to japan."
print(id(game))

def game_board():
    global game         #by using global now we will be able to change the value of game
    game = "noob"
    print(game)
    print(id(game))

game_board()
print(game)
print(id(game))
'''

'''
game = [[0,0,0],
        [0,0,0],
        [0,0,0],]



def game_board(player=0,row=0,column=0,just_player = False): 
    if not just_player:
        game[row][column] = player
    print('   a  b  c')
    for count, row in enumerate(game):
        print(count, row)


game_board(1,0,0)
game_board( just_player = True)
'''

'''
x = 1
def test():
    x = 2
test()
print(x)


x = 1
def test():
    global x
    x = 2
test()
print(x)


x = [1]
def test():
    x = [2]
test()
print(x)


x = [1]
def test():
    global x
    x = [2]
test()
print(x)


x = [1]
def test():
    x[0] = 2
test()
print(x)
'''