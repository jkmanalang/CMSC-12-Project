import random
import os

def table_display (field):								# will be used to display field
	os.system("cls")
	row = 1
	column = [x for x in range (1, len(field[1])+1)]
	print ("\t", end="  ")
	for i in column:									# to display the column numbers
		if i//10 == 0:
			print (i, end="   ")
		else:
			print (i, end="  ")
	print ("\n\n\n\t", ("-" * (len(field[0])*4)))		# lines for appearance

	for i in field:										# will display the row per column (one by one)
				
		print (row, end="\t| ")
		row += 1
		for j in i:
			print (j, end=" | ")
		print ()

		print ("\t", ("-" * (len(i)*4)))


def get_mines(row, column, num_of_mines):					# will be used to generate mines and their locations

	counter = 0
	mine_list = []											

	while counter < num_of_mines:
		(crow, ccolumn) = random.randint(0,row-1), random.randint(0,column-1)		# randomly makes a pair of row and column

		if (crow,ccolumn) not in mine_list:											# check if the pair is already in the mine_list
			mine_list.append((crow,ccolumn))
			counter += 1
	return mine_list


def set_field (mine_locations, row, column):								# will be used to give values to the index of mines, and the surrounding areas of that mine
	field = [[0 for x in range (0,column)] for i in range (0, row)]			# also makes the list of lists that will serve as the field

	for mine in mine_locations:
		(crow_mine, ccol_mine) = mine

		field[crow_mine][ccol_mine] = "+"						# marks the mines

		surrouding_row = range (crow_mine-1, crow_mine+2)		# range of the areas surrounding the mine (row)
		surrouding_colm = range (ccol_mine-1, ccol_mine+2)		# (column)

		for i in surrouding_row:								# incrementing the surrounding row/column of the mine by 1
			for j in surrouding_colm:

				if (0 <= i < row and 0 <= j < column and field[i][j] != "+"):
					field[i][j] += 1
	return field


def get_user_answer(needed_input, min_range, max_range, necessary_info):			# will be used to get desired outputs
	while True:																		# and avoid sudden error when the program is running
		try:
			user_answer = int (input (needed_input + ": "))
			while min_range > user_answer or user_answer > max_range:
				user_answer = int (input ("\n" + necessary_info + "\n" + needed_input + ": "))
			break
		except:
			print ("\nPlease enter an Integer.")
	return user_answer


def location_checker(field):				# to get the user_column and user_row and to check if it is in the range of the field
	field_row = len(field)
	field_column = len(field[0])

	row = get_user_answer("Row", 1, field_row, "Row must only be between 1-" + str(field_row) + " due to row limitation")
	column = get_user_answer("Column", 1, field_column, "Column must only be between 1-" + str(field_column) + " due to column limitation")
	return row, column	


def empty_field_update(empty_field, user_row, user_column, update):			# to update the row,column location in empty field
	goto_row = empty_field.pop(user_row-1)									# by using the input row and column and find the value
	rmv_specific_slot = goto_row.pop(user_column-1)							# in field
	goto_row.insert(user_column-1, update)
	empty_field.insert(user_row-1, goto_row)
	return empty_field


def dug_locations (empty_field, field):					# to count the numbers of locations that has already been dug
	count = 0
	row = len(empty_field)
	column = len(empty_field[1])
	for i in range (0, row):
		for j in range (0, column):
			if empty_field[i][j] == field[i][j]:
				count += 1
	return count