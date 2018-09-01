#python dependencies
import sys
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
		# self.sudokuGrid.setItemDelegate(Delegate())
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

				#set the item to the value
				item = QtWidgets.QTableWidgetItem()
				item.setData(QtCore.Qt.EditRole, str(value))
				item.setTextAlignment(QtCore.Qt.AlignCenter)
				
				#checking if move has been made
				if value != 0:
					self.sudokuGrid.setItem(row, col, item)
				else: 
					self.sudokuGrid.setItem(row, col, QtWidgets.QTableWidgetItem(0))

				if not cell.isPlayable:
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

				# if cell.isPlayable:
				if cell.isPlayable:
					self.sudokuGrid.item(row, col).setText("")
					
					cell.setValue(0)
		# defaultBoard.clear()

	#updates a cell in the ui
	def change(self, row, col):
		
		number = self.sudokuGrid.item(row, col).text()
		cell = defaultBoard.board[row][col]

		if number != '':
			number = int(number)	
			cell.setValue(number)
		else:
			cell.setValue(0)

		# self.updateGrid(defaultBoard)
		
	#saves the game to a csv
	def save(self):
		filename = self.saveText.text()
		print(filename)
		defaultBoard.save(filename)

	#loads in a csv as a playable game
	def load(self):
		filename = self.loadText.text()
		defaultBoard.load(filename)
		self.updateGrid(defaultBoard)

	#checks to see if a submited board is valid
	def submit(self):
		result = defaultBoard.isCorrect()
		#if solution is correct
		if result:
			QtWidgets.QMessageBox().about(self, "Success", "Congratulations! You solved the puzzle")
		#if solution is incorrect
		else:
			QtWidgets.QMessageBox().about(self, "Oops", "Not a valid solution.  Click OK to keep trying.")



# class Delegate(QtWidgets.QItemDelegate):

# 	lineEdit = QtWidgets.QLineEdit()
# 	# validator = QtGui.QIntValidator(1,9, QtWidgets.QLineEdit())
# 	pass

#main method, creates a board object and gui object to play the game
if __name__ == '__main__':
	defaultBoard = Board('board_values.csv')
	sudokuApp = QtWidgets.QApplication(sys.argv)
	gui = Window()
	sys.exit(sudokuApp.exec_())