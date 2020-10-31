import itertools

def win(current_map):

	# Horizontal
	for row in current_map:
		if row.count(row[0]) == len(row) and row[0] != 0:			#only one line of code
			print(f'Player {row[0]} is the winner horizontally (-)!')					

	# Vertical
	for col in range(len(current_map)):
		check = []
		for row in current_map:
			check.append(row[col])
		if check.count(check[0]) == len(check) and check[0] != 0:
			print(f'Player {check[0]} is the winner vertically (|)!')

	# Diagonal
	diags = []
	for idx in range(len(current_map)):
		diags.append(current_map[idx][idx])

	if diags.count(diags[0]) == len(diags) and diags[0] != 0:
		print(f'Player {diags[0]} is the winner diagonally (\\)!')			# backslash(\) is usually used for escaping the value and prefixing the special 
																			# with '\' changes the character into ordinary character
	diags = []
	for row, col in enumerate(list(reversed(range(len(current_map))))):
		diags.append(game[row][col])

	if diags.count(diags[0]) == len(diags) and diags[0] != 0:
		print(f'Player {diags[0]} is the winner diagonally (/)!')

def game_board(game_map, player = 0, row = 0, column = 0, just_display = False):
	try:
		if not just_display:
			game_map[row][column] = player
		print('   0  1  2')
		for count, row in enumerate(game_map):
			print(count, row)
		print('\n')
		return game_map

	except IndexError as e:
		print('Error: Make sure you input row/column as 0,1 & 2;', e)
	except Exception as e:
		print('Something is very very wrong!! ',e)


play = True
players = itertools.cycle([1,2])
while play:

	game = [[0,0,0],
			[0,0,0],
			[0,0,0]]
	game_won = False
	game = game_board(game,just_display = True)
	while not game_won:
		
		current_player = next(players)
		print('Current Player:',current_player)
		column_choice = int(input('What column do you want to play (0,1,2): '))
		row_choice = int(input('What row do you want to play (0,1,2): '))
		game = game_board(game, current_player, row_choice, column_choice)


'''
# First approach of flipping between 1 and 2 is 
players = [1,0]

choice = 1
for i in range(10):
	current_player = choice + 1
	print(current_player)
	choice = players[choice]				#this line is flipper
'''

'''
# Second approach of flipping between numbers
players = itertools.cycle([1,2])

for i in range(10):
	print(next(players))
'''

'''
# iterable: a thing we can iterate over
# iterator: a special object with next() method

x = [1,2,3,4,5]								#this is an iterable

#print(next(x))								#TypeError: 'list' object is not an iterator
z = itertools.cycle([1,2,3,4,5])			#this is an iterator as well as iterable
y = iter(x)									#this is an iterator as well as iterable

print(next(y))
#print(next(y))
#print(next(y))
#print(next(y))
#print(next(y))
print('')

for i in y:
	print(i)								#this is stops printing after values is finished
#print(next(y))								#this is showing error because we have converted iterable to an iterator

print(next(z))
print(next(z))
print(next(z))
print(next(z))
print(next(z))
print(next(z))
print(next(z))
print("")

#for i in z:
	#print(i)
'''