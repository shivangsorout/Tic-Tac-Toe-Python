'''

def add(x,y):
    return(x+y)

print(add("Hello"," Noob"))     #we can also add strings
print(add(5,4))
print(add("Hello",4))           #this will give you error

'''


game = [[0,0,0],
        [0,0,0],
        [0,0,0],]



def game_board(player=0,row=0,column=0,just_player = False):  #default value
    if not just_player:
        game[row][column] = player
    print('   a  b  c')
    for count, row in enumerate(game):
        print(count, row)


game_board(1,0,0)
game_board( just_player = True)
