# File:    proj3.py
# Author:  Ujjwal Rehani
# Date:    5/6/2017 
# Section: 21
# E-mail:  urehani1@umbc.edu 
# Description:
#   This project simulates a game of minesweeper

# printGreeting() explains the program to the user
# Input:          none
# Output:         none (prints greeting)
def printGreeting():
	print()
	print("\tThis program allows you to play Minesweeper.")
	print("\tThe object of the game is to flag every mine,")
	print("\tusing clues about the number of neighboring")
	print("\tmines in each field.  To win the game, flag")
	print("\tall of the mines (and don't incorrectly flag")
	print("\tany non-mine fields).  Good luck!")
	print()

# loadFile() reads in file and creates 2d list
# Input:          			none
# Output:  gameBoard       a 2d list that represents the game board
def loadFile():
	gameBoard = []
	#copy of the board
	mineBoard = [] 
	fileName = input("Enter the file to load the board from: ")
	myFile = open(fileName,"r")
	
	#creates two boards
	for line in myFile:
		row = []
		rowCopy = []
		line = line.strip()
		for index in line:
			row.append(index)
			rowCopy.append(index)
		gameBoard.append(row)
		mineBoard.append(rowCopy)
	

	return gameBoard, mineBoard
		
# userBoard() creates a playable board the same size as the board with mines
# Input:   board        	board to be changed into a playbale board	
# Output:  board                board that is ready to be used  	
def userBoard(givenBoard):
	
	#creates a playable board for game
	count = 0
	while(count < len(givenBoard)):
		count2=0
		while(count2<len(givenBoard[count])):
			if( " " in givenBoard[count][count2] or "*" in givenBoard[count][count2]):
				givenBoard[count][count2] = "."	
			count2+=1
		count+=1
	
	#num of selectable rows and cols are always 2 less than the actual num of rows and cols
	numRows = (len(givenBoard)-2)
	numCol = (len(givenBoard[0])-2)
		
	return numRows, numCol, givenBoard
	
def makeChoice(numRows,numCol):
	print("Please choose the row: ")
	validRow, validCol = getValidInt(numRows,numCol)
	
	print()
	print("Enter 'r' to reveal the space, or")
	choice = input("enter 'f' to mark the space with a flag: ")
	#Checks for valid input
	while(choice != "r" and choice != "f"):
		print("That's not a valid action.")
		print("Enter 'r' to reveal the space, or")
		choice = input("enter 'f' to mark the space with a flag: ")
	
	print()
	return choice, validRow, validCol
	
# getValidInt() reprompts the user until they enter a number
#               valid for row and column
# Input:        rows,cols	num of rows and columns from board
# Output:       rowNum, colNum; valid row and column numbers
def getValidInt(rows,cols):

	#Checks for valid row
	rowNum = int(input("Enter a number between 1 and "+str(rows)+" (inclusive): "))
	while(rowNum < 1 or rowNum > rows):
		print("That number is not allowed.  Please try again!")
		rowNum = int(input("Enter a number between 1 and "+str(rows)+" (inclusive): "))
	
	#Checks for valid column
	print()
	print("Please choose the column: ")
	colNum = int(input("Enter a number between 1 and "+str(cols)+" (inclusive): "))
	while(colNum < 1 or colNum > cols):
		print("That number is not allowed.  Please try again!")
		colNum = int(input("Enter a number between 1 and "+str(cols)+" (inclusive): "))
	
	return rowNum, colNum

# updateBoard() 	updates board based on the user selection    
#                   
# Input:             playBoard, givenBoard, userChoice,valRow,valCol; two boards to be compared, user selection, valid row/col entries      
# Output:            numMines;  num of mines flagged
def updateBoard(playBoard, mineBoard, userChoice,valRow,valCol,numMines):

	#Updates board with correct symbol based on choice
	if(userChoice == "f" and playBoard[valRow][valCol] != "F" and mineBoard[valRow][valCol] != "*"):
		playBoard[valRow][valCol] = "F"
	elif(userChoice == "f" and playBoard[valRow][valCol] != "F" and mineBoard[valRow][valCol] == "*"):
		playBoard[valRow][valCol] = "F"
	elif(userChoice == "r" and playBoard[valRow][valCol] == "F" ):
		print("\tField",valRow,",",valCol,"must be unflagged before it can be revealed")
	elif(userChoice == "f" and playBoard[valRow][valCol] == "F" ):
		playBoard[valRow][valCol] = "."
		print("\tFlag removed from",valRow,",",valCol)
	elif(userChoice == "r"):
		playBoard[valRow][valCol] = " "

	return numMines
	
# makeIsland() 	recursively clears empty space
#                   
# Input:             board;      
# Output:            newBoard;    updated board with cleared space
def makeIsland(board):
	print()
	#basecase
	
	#recursive case
	
# checkBoard() 	     Check conditions for game over or game won  
# Input:             playBoard, mineBoard;   board which the user plays on and the board containing mines     
# Output:            minesFlagged, gameOver, playBoard; num of mines user has flagged, bool representing if game is over, and the game board
def checkBoard(playBoard,mineBoard):
	
	minesFlagged = 0
	
	#bool to determine if game is over
	gameOver = False 
	count = 0
	while(count < len(playBoard)):
		count2=0
		while(count2<len(playBoard[count])):
			#Checks if mine is detonated or if mine has been flagged
			if(playBoard[count][count2]  == " " and mineBoard[count][count2] == "*"):
				playBoard[count][count2]  = "X"
				print("You detonated a mine!  Game Over!")
				gameOver = True
			if(playBoard[count][count2]  == "F" and mineBoard[count][count2] == "*"):
				minesFlagged += 1
				
			count2+=1
		count+=1
	
	return minesFlagged, gameOver, playBoard
# prettyPrintBoard() prints the board with row and column labels,      #
#                    and spaces the board out so that it looks square  #
# Input:             board;   the rectangular 2d gameboard to print    #
# Output:            none;    prints the board in a pretty way         #
def prettyPrintBoard(board):
	# if board is large enough, print a "tens column" line above the rows
	if len(board[0]) - 2 >= 10:
		firstLine = "\n     " + ("  ") * (10 - 1)
		for i in range(10, len(board[0])-1 ):
			firstLine += str(i // 10) + " "
		print(firstLine, end="")

	# create and print top numbered line (and empty line before)
	topLine = "\n     "
	# only go from 1 to len - 1, so we don't number the borders
	for i in range(1, len(board[0])-1 ):
		# only print the last digit (so 15 --> 5)
		topLine += str(i % 10) + " "
	print(topLine)

	# create the border row
	borderRow = "   "
	for col in range(len(board[0])):
		borderRow += board[0][col] + " "

	# print the top border row
	print(borderRow)

	# print all the interior rows
	for row in range(1, len(board) - 1):
		# create the row label on the left
		rowStr = str(row) + " "

		# if it's a one digit number, add an extra space, so they line up
		if row < 10:
			rowStr += " "

		# add the row contents to the row string, and print it out
		for col in range(len(board[row])):
			rowStr += str(board[row][col]) + " "
		print(rowStr)

	# print the bottom border row and an empty line
	print(borderRow)
	print()
	
def main():
	printGreeting()
	givenBoard, mineBoard  = loadFile()
	row,col,playBoard = userBoard(givenBoard)
	
	#calculates num of mines present
	numMines = 0
	for rows in mineBoard:
		for cols in rows:
			if(cols == "*"):
				numMines += 1 
				
	minesFlagged, gameOver, playBoard = checkBoard(playBoard, mineBoard)
	#Game contines until mine is detonated or if all mines have been flagged
	while(minesFlagged != numMines and gameOver == False):
		print("There are",numMines,"mines to find")
		prettyPrintBoard(playBoard)
		userChoice,valRow,valCol = makeChoice(row,col)
		numMines = updateBoard(playBoard, mineBoard, userChoice, valRow, valCol, numMines) 
		minesFlagged, gameOver, playBoard = checkBoard(playBoard, mineBoard)
	
	if(minesFlagged == numMines):
		print("You won! Congratulations, and good game!")
		
	prettyPrintBoard(playBoard)

main()
