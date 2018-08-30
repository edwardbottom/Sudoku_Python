from Cell import Cell
import pandas as pd


class Board:
  def __init__(self):
    self.board = []
    vals = pd.read_csv('board_values.csv')
    vals_length = int(vals.count())
    counter = 0
    for x in range(0,9): 
    	row=[]
    	for y in range(0,9):
    		val = int(str(vals.values[(counter)]).strip("[]").strip("''"))
    		row.append(Cell(val,False))
    		counter += 1
    	self.board.append(row)

  def printBoard(self):
  	for y in range(0,9):
  		string =''
  		for x in range(0,9):
  			if self.board[x][y].value == 0:
  				string += ' '
  			else:
  				string += ' ' + str(self.board[x][y].value)
  		print(string)

  def clear(self):
  	self.board = []
  	vals = pd.read_csv('board_values.csv')
  	vals_length = int(vals.count())
  	counter = 0
  	for x in range(0,9): 
  		row=[]
  		for y in range(0,9):
  			val = int(str(vals.values[(counter)]).strip("[]").strip("''"))
  			row.append(Cell(val,False))
  			counter += 1
  		self.board.append(row)

  def load(self):
  	self.board = []
  	vals = pd.read_csv('board_values.csv')
  	vals_length = int(vals.count())
  	counter = 0
  	for x in range(0,9): 
  		row=[]
  		for y in range(0,9):
  			val = int(str(vals.values[(counter)]).strip("[]").strip("''"))
  			row.append(Cell(val,False))
  			counter += 1
  			self.board.append(row)
  
  def save(self, file_name):
  	vals = []
  	for x in range(0,9): 
  		for y in range(0,9):
  			val = self.board[x][y].value
  			vals.append(val)
  	df = pd.DataFrame(vals)
  	df.to_csv(file_name)
  
  def isValidHorz(self):
  	s = set()
  	for y in range(0,9):
  		for x in range(0,9):
  			if self.board[x][y].value > 9 or self.board[x][y].value < 1 or not s.add(self.board[x][y].value):
  				return False
  		s.clear()
  	return True

  def isValidVert(self):
    s = set()
    for x in range(0,9):
        for y in range(0,9):
            if self.board[x][y].value > 9 or self.board[x][y].value < 1 or not s.add(self.board[x][y].value):
                return False
        s.clear()
    return True

  def isValidBox(self):
    s = set()
    #upper left box
    for x in range(0,3):
        for y in range(0,3):
            if self.board[y][x].value > 9 or self.board[y][x].value < 1 or not s.add(self.board[y][x].value):
                return False
    s.clear()

    #upper middle box
    for x in range(3,6):
        for y in range(0,3):
            if self.board[y][x].value > 9 or self.board[y][x].value < 1 or not s.add(self.board[y][x].value):
                return False
    s.clear()

    #upper right box
    for x in range(6,9):
        for y in range(0,3):
            if self.board[y][x].value > 9 or self.board[y][x].value < 1 or not s.add(self.board[y][x].value):
                return False
    s.clear()

    #middle left box
    for x in range(0,3):
        for y in range(3,6):
            if self.board[y][x].value > 9 or self.board[y][x].value < 1 or not s.add(self.board[y][x].value):
                return False
    s.clear()

    #middle middle box
    for x in range(3,6):
        for y in range(3,6):
            if self.board[y][x].value > 9 or self.board[y][x].value < 1 or not s.add(self.board[y][x].value):
                return False
    s.clear()

    #middle right box
    for x in range(6,9):
        for y in range(3,6):
            if self.board[y][x].value > 9 or self.board[y][x].value < 1 or not s.add(self.board[y][x].value):
                return False
    s.clear()

    #bottom left box
    for x in range(0,3):
        for y in range(6,9):
            if self.board[y][x].value > 9 or self.board[y][x].value < 1 or not s.add(self.board[y][x].value):
                return False
    s.clear()

    #bottom middle box
    for x in range(3,6):
        for y in range(6,9):
            if self.board[y][x].value > 9 or self.board[y][x].value < 1 or not set.add(self.board[y][x].value):
                return False
    set.clear()

    #bottom right box
    for x in range(6,9):
        for y in range(6,9):
            if self.board[y][x].value > 9 or self.board[y][x].value < 1 or not s.add(self.board[y][x].value):
                return False
    s.clear()

    return True

  def isCorrect(self):
    return self.isValidBox() and self.isValidHorz() and self.isValidVert()

Board().save("board_values.csv")