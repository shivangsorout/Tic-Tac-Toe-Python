# Slicing and Indexing
'''
fps = ['PUBG', 'Valorant', 'Call of duty', 'Freefire']

print(fps[0:3])         Slicing from 0 to 2
print(fps[0:])          Slicing from 0 to end
print(' 3: '+fps[3])    
print('-1: '+fps[-1])

'''






game = [[0,0,0],
        [0,0,0],
        [0,0,0],]

print('   a  b  c')

game[0][1] = 1   #indexing


for count, row in enumerate(game):
    print(count, row)
