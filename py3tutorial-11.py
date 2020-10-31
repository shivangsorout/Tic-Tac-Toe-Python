# Tic Tac Toe- Vertical Winner

game = [[1,0,0],
        [1,0,0],
        [1,0,0],]

'''
#first and hard coded approach not dynamic

column = [0,1,2]

for col in column:
    check = []

    for row in game:
        check.append(row[col])

    if check.count(check[0]) == len(check) and check[0] != 0:
        print('Winner')
'''

'''
#range is not actually a function but we treat it like one

x = range(3)
for i in x:
    print(i)

'''

#second and best approach 

for col in range(len(game)):
    check = []

    for row in game:
        check.append(row[col])

    if check.count(check[0]) == len(check) and check[0] != 0:
        print('Winner')
