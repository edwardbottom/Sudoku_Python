#python dependencies
import sys
import re
from PyQt5.uic import loadUi
from PyQt5 import QtGui, QtWidgets, QtCore
from Board import Board

#creates a class for the gui
class Window(QtWidgets.QWidget):
	
	#constructor for the gui
	def __init__(self):

		super(Window, self).__init__()
		loadUi('sudoku.ui', self)
		
		#event listeners for buttons
		self.quitButton.clicked.connect(self.quit)
		self.clearButton.clicked.connect(self.clear)
		self.saveButton.clicked.connect(self.save)
		self.loadButton.clicked.connect(self.load)
		self.submitButton.clicked.connect(self.submit)
		self.updateGrid(defaultBoard)
		self.sudokuGrid.cellChanged.connect(self.change)

	#updates the board based on a users submissions
	def updateGrid(self, board):
		#check each value in the grid
		for row in range(0,9):
			for col in range(0,9):
				cell = board.board[row][col]
				value = cell.getValue()

				#create table widget item
				item = QtWidgets.QTableWidgetItem()
				item.setTextAlignment(QtCore.Qt.AlignCenter)
				
				#set the value of the items
				if int(value) != 0:
					item.setData(QtCore.Qt.DisplayRole, str(value))
				else:
					item = QtWidgets.QTableWidgetItem("")

				self.sudokuGrid.setItem(row, col, item)

				#mark appropriate cells as not playable
				if cell.isPlayable == "FALSE":
					self.sudokuGrid.item(row, col).setFlags(QtCore.Qt.ItemIsEnabled)
				
		self.show()

	#closes the game
	def quit(self):
		self.close()

	#clears the entire board of playable cells
	def clear(self):
		for row in range(0,9):
			for col in range(0,9):

				cell = defaultBoard.board[row][col]
				item = self.sudokuGrid.item(row, col)

				#if the cell is playable, clear the contents of the cell and update the value of the cell to 0
				if cell.isPlayable == "TRUE":
					item.setText("")
					item.setTextAlignment(QtCore.Qt.AlignCenter)
					cell.setValue(0)

	#updates a cell in the ui
	def change(self, row, col):
		
		#get the cell that the user is trying to change
		item = self.sudokuGrid.item(row, col)
		userInput = item.text()
		cell = defaultBoard.board[row][col]

		#if the user input is not an integer between 0-9, the cell gets cleared
		if not isValidInput(userInput):
			item.setText("")
			return

		#if the input is valid, set the cell's value to the input
		if input != '':
			number = int(userInput)	
			cell.setValue(number)
			item.setTextAlignment(QtCore.Qt.AlignCenter)
		else:
			cell.setValue(0)
		
	#saves the game to a csv
	def save(self):
		filename = self.saveText.text()
		# print(filename)
		defaultBoard.save(filename)

	#loads in a csv as a playable game
	def load(self):
		filename = self.loadText.text()
		defaultBoard.load(filename)
		self.updateGrid(defaultBoard)

	#checks to see if a submited board is valid
	def submit(self):
		result = defaultBoard.isCorrect()

		#if the solution is valid, an image of Dan pops up
		if result:
			box = QtWidgets.QMessageBox()
			image = QPixmap("dan_photo.jpg")
			scaledImage = image.scaled(QtCore.QSize(700,700),  QtCore.Qt.KeepAspectRatio)
			box.setIconPixmap(scaledImage)
			box.show()
			box.exec()
			box.about(self, "Success", "Congratulations! You solved the puzzle")

		#error message if solution is invalid
		else:
			QtWidgets.QMessageBox().about(self, "Oops", "Not a valid solution.  Click OK to keep trying.")


#checks whether or not the input is an integer between 1-9
def isValidInput(input):
	return re.match(r'^[1-9]$', input)


#main method, creates a board object and gui object to play the game
if __name__ == '__main__':
	defaultBoard = Board('board_values.csv')
	sudokuApp = QtWidgets.QApplication(sys.argv)
	gui = Window()
	sys.exit(sudokuApp.exec_())