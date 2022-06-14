"""
Program: Minesweeper (A.Y. 2020-2021 First Semester) 

John Kenneth F. Manalang

"""

import os
import game_code
import game_functions

while True:

	print ("""													
		\n===================Game Mode====================
   [1] New Game
   [2] Load Game File
   [0] Exit
================================================\n""")

	user_choice = game_functions.get_user_answer("Choice", 0, 2, "Please input 0-2 only.")

	if user_choice == 1:

		while True:
			print ("""													
			\n===================Game Mode====================
   [1] Beginner
   [2] Intermediate
   [3] Expert
   [4] Custom
   [0] Back
================================================\n""")

			user_choice = game_functions.get_user_answer("Choice (0-4)", 0, 4, "Invalid Input")


			if user_choice == 1:				# field making for 8x8 board size (beginner)
				row = 8
				column = 8
				mines = 8

			elif user_choice == 2:				# field making for 12x12 board size (intermediate)	
				row = 12
				column = 12
				mines = 12

			elif user_choice == 3:				# field making for 16x16 board size (expert)
				row = 16
				column = 16
				mines = 30

			elif user_choice == 4:				# field making for custom board size
				row = game_functions.get_user_answer("\nRow: ", 2, 50, "Row must only be between 2-50 due to screen limitation")
				column = game_functions.get_user_answer("Column: ", 2, 50, "Column must only be between 2-50 due to screen limitation")
				mines = game_functions.get_user_answer("Mines", 0, (row*column)-1, "Mines must only be between 0-" + str((row*column)-1) + " due to field limitation")

			else:
				break

			empty_field = [[" " for x in range (0,column)] for i in range (0, row)]						# creating the empty field
			field = game_functions.set_field(game_functions.get_mines(row,column, mines), row, column)	# creating the field
			

			game_code.game(row, column, mines, empty_field, field)


	elif user_choice == 2:
		game_code.load_game()
		
	else:
		print ("\nThank you for playing!\n")
		break