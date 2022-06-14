import os
import game_functions
import ast

def dig (dug_locations, empty_field, field, row, column):				# will be use in digging the specified location
	if (row, column) not in dug_locations:
		dug_locations.append((row, column))
	num = [1,2,3,4,5,6,7,8]
	if field[row-1][column-1] == '+':									# return False if the dug location is a mine
		return False
	elif field[row-1][column-1] in num:									# return True if safe 			
		return True

	for r in range (row-1, row+2):										# recursively dig if the dug location is not near a mine
		for c in range (column-1, column+2):
			if (0 < r <= len(field) and 0 < c <= len(field[0])):
				if (r, c) in dug_locations:
					continue

				dig (dug_locations, empty_field, field, r, c)
	return True


def game(row, column, mines, empty_field, field):						# code for the game	
	must_be_dug = (row*column)-mines
	dug_locations = []
	safe = True															# will be used to determine the current status of the player 

	while game_functions.dug_locations(empty_field, field) != must_be_dug:						# continues until locations are all dug
		game_functions.table_display(empty_field)
		user_row, user_column = game_functions.location_checker(field)							# get the user row and column input
			
		if empty_field[user_row-1][user_column-1] == field[user_row-1][user_column-1]:			
			continue

		if empty_field[user_row-1][user_column-1] != "F":

			choice = game_functions.get_user_answer("1 = Save, 2 = Flag, 3 = Dig\nChoice (1-3)", 1, 3, "Invalid Input")

				
			if choice == 3:																	# for digging
				safe = dig(dug_locations, empty_field, field, user_row, user_column)
					
				for i in dug_locations:
					row, column = i
					game_functions.empty_field_update(empty_field, row, column, field[row-1][column-1])
				game_functions.table_display(empty_field)
					
					
				if not safe:
					break

			elif choice == 2:																# for inserting flag
				game_functions.empty_field_update(empty_field, user_row, user_column, "F")

			else:																			# save the game
				fileHandler = open("MSfile_emptyfile.txt", "w")
				for row in empty_field:
					fileHandler.write(str(row) + "\n")
				fileHandler.close()

				fileHandler2 = open("MSfile_field.txt", "w")
				for row in field:
					fileHandler2.write(str(row) + "\n")
				fileHandler2.close()

				safe = 'save'
				break

		else:
			game_functions.empty_field_update(empty_field, user_row, user_column, " ")

	if safe == True:
		print ("\nCongratulation you won!")
	elif safe == 'save':
		print ("\n\nCurrent game saved.")
	else:
		game_functions.table_display(field)
		print("\nYou dead")


def load_game():										# load function
	fileHandler = open("MSfile_emptyfile.txt", "r")
	load_empty_field = fileHandler.readlines()
	empty_field = []

	for i in load_empty_field:							# getting the saved empty field
		row = ast.literal_eval(i)
		empty_field.append(row)
	fileHandler.close()

	fileHandler2 = open("MSfile_field.txt", "r")
	load_field = fileHandler2.readlines()
	field = []

	for i in load_field:								# getting the saved field
		row = ast.literal_eval(i)
		field.append(row)
	fileHandler2.close()

	row = len(field)
	column = len(field[0])
	mines = 0
	for i in field:
		for j in i:
			if j == '+':
				mines += 1

	game(row, column, mines, empty_field, field)		# the game			
	return