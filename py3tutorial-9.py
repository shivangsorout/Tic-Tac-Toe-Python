#Error Handling

game = [[0,0,0],
		[0,0,0],
		[0,0,0],]

def game_board(game_map, row=0, column=0, player=0, just_display=False):
	try:
		if not just_display:
			game_map[row][column] = player
		print('   0  1  2')
		for count, row in enumerate(game_map):
			print(count, row)
		#raise Exception			#for raising an error purposely
		return game_map
	except IndexError as e:
		print('Error: Make sure you input row/column as 0,1 & 2;',e)
	except Exception as e:
		print('Error: Something went very wrong!!',e)
	#else:							#rarely used			

	#finally:						#rarely used

game = game_board(game,just_display = True)
game = game_board(game_board,0,4,1)
