#Basically we are creating a tic tac toe game.

# Difference between Tuple(same as list but immutable) and List

#Tuple
game = (0,0,0,
       0,0,0,
       0,0,0,)

print(game)
print(type(game))

#List
game = [[0,0,0],
        [0,0,0],
        [0,0,0],] #we are using this because we have to show in that format

print(game)
print(type(game))

for row in game:
    print(row)