import sys
from PyQt5.uic import loadUi
from PyQt5 import QtGui, QtWidgets, QtCore
from Board import Board


class Window(QtWidgets.QWidget):
	
	def __init__(self):

		super(Window, self).__init__()
		loadUi('sudoku.ui', self)
		
		# self.sudokuGrid.setItemDelegate(Delegate())
		self.quitButton.clicked.connect(self.quit)
		self.clearButton.clicked.connect(self.clear)
		self.saveButton.clicked.connect(self.save)
		self.loadButton.clicked.connect(self.load)
		self.submitButton.clicked.connect(self.submit)
		self.updateGrid(defaultBoard)
		self.sudokuGrid.cellChanged.connect(self.change)

	
	def updateGrid(self, board):
			
		for row in range(0,9):
			for col in range(0,9):
				cell = board.board[row][col]
				value = cell.getValue()

				item = QtWidgets.QTableWidgetItem()
				item.setData(QtCore.Qt.EditRole, str(value))
				item.setTextAlignment(QtCore.Qt.AlignCenter)
				
				if value != 0:
					self.sudokuGrid.setItem(row, col, item)
				else: 
					self.sudokuGrid.setItem(row, col, QtWidgets.QTableWidgetItem(0))

				if not cell.isPlayable:
					self.sudokuGrid.item(row, col).setFlags(QtCore.Qt.ItemIsEnabled)
				
		self.show()


	def quit(self):
		self.close()


	def clear(self):
		for row in range(0,9):
			for col in range(0,9):

				cell = defaultBoard.board[row][col]

				# if cell.isPlayable:
				if cell.isPlayable:
					self.sudokuGrid.item(row, col).setText("")
					
					cell.setValue(0)

	
	def change(self, row, col):
		
		number = self.sudokuGrid.item(row, col).text()
		cell = defaultBoard.board[row][col]

		if number != '':
			number = int(number)	
			cell.setValue(number)
		else:
			cell.setValue(0)

		self.updateGrid(defaultBoard)
		
	
	def save(self):
		filename = self.saveText.text()
		print(filename)
		defaultBoard.save(filename)

	def load(self):
		filename = self.loadText.text()
		defaultBoard.load(filename)
		self.updateGrid(defaultBoard)

	def submit(self):
		result = defaultBoard.isCorrect()

		if result:
			QtWidgets.QMessageBox().about(self, "Success", "Congratulations! You solved the puzzle")
		else:
			QtWidgets.QMessageBox().about(self, "Oops", "Not a valid solution.  Click OK to keep trying.")



# class Delegate(QtWidgets.QItemDelegate):

# 	lineEdit = QtWidgets.QLineEdit()
# 	# validator = QtGui.QIntValidator(1,9, QtWidgets.QLineEdit())
# 	pass

if __name__ == '__main__':
	defaultBoard = Board('board_values.csv')
	sudokuApp = QtWidgets.QApplication(sys.argv)
	gui = Window()
	sys.exit(sudokuApp.exec_())