# Tic Tac Toe - Diagonal Winners


#This is for the first diagonal

game = [[1,0,0],
        [0,1,0],
        [0,0,1],]

diags = []

for idx in range(len(game)):
    diags.append(game[idx][idx])

if diags.count(diags[0]) == len(diags) and diags[0] != 0:
        print('Winners')



#This is for the second diagonal and full explanation is given below

game = [[0,0,1],
        [0,1,0],
        [1,0,0],]

diags = []

for row, col in enumerate(list(reversed(range(len(game))))):
    diags.append(game[row][col])

if diags.count(diags[0]) == len(diags) and diags[0] != 0:
    print('Winners')



'''
#this is how the reversed funtion work

for i in reversed(range(len(game))):
    print(i)
'''

'''
game = [[0,0,1],
        [0,1,0],
        [1,0,0],]

cols = reversed(range(len(game)))   # so reversed is not a list type that is why it is showing type error while range works
rows = range(len(game))

for i in rows:
    print(i, cols[i])               #TypeError: 'range_iterator' object is not subscriptable
'''

'''
#this is good but this too long code


game = [[0,0,1],
        [0,1,0],
        [1,0,0],]


cols = list(reversed(range(len(game))))
rows = range(len(game))

for i in rows:
    print(i,cols[i])

'''

'''
#explaining about zip

x = [0,2,4]
y = [9,8,3]
z = [7,8,9]

#for i in zip(x,y,z):
    #print(i)
for i,j,k in zip(x,y,z):
    print(i,j,k)
'''

'''
game = [[0,0,1],
        [0,1,0],
        [1,0,0],]

#cols = list(reversed(range(len(game))))
#rows = range(len(game))

#for row,col in zip(rows,cols):
    #print(row,col)

#or even shorter version is :-

#for row, col in zip(range(len(game)),list(reversed(range(len(game))))):
    #print(row,col)

#but we can do same work using enumerate(), so

for row, col in enumerate(list(reversed(range(len(game))))):
    print(row, col)
'''
