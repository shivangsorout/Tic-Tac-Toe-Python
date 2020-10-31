# Tic Tac Toe - Horizontal Winner

game = [[1,1,1],
		[0,0,0],
		[3,2,0],]

'''
#first simplest ,slowest and non dynamic approach

def win(current_map):
	for row in current_map:
		print(row)
		for item in row:
			item1 = row[0]
			item2 = row[1]	
			item3 = row[2]
		if item1 == item2 == item3:
			print('Winner!!')
'''

'''
#second approach but its so much of code such a small thing

def win(current_map):
	for row in current_map:
		print(row)
		all_match = True							#-------
		for item in row:							#		|
			if item != row[0]:						#		| this is the code
				all_match = False					#		|
		if all_match:								#      	|
			print('Winner!!')						#-------
'''
#best approach using google for checking a list for all same items

def win(current_map):
	for row in current_map:
		print(row)
		if row.count(row[0]) == len(row) and row[0] != 0:			#only one line of code
			print('Winner')					


win(game)