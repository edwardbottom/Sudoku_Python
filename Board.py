#python dependencies
from Cell import Cell
import pandas as pd
import os

#class for the board object
class Board:
  #constructor that creates cells from a csv
  def __init__(self, file_name):
    #intialize the board and get the data
    self.board = []
    vals = pd.read_csv(file_name)
    vals_length = vals.count().astype(int)
    counter = 0
    #fill the board with the data
    for x in range(0,9): 
      row=[]
      for y in range(0,9):
        val = vals['b'][counter]
        isPlay = vals['b'][counter+1]
        # val = int(str(vals.values[(counter)]).strip("[]").strip("''"))
        row.append(Cell(val,isPlay))
        counter += 2
      self.board.append(row)

  #debug function for printing the board to the console
  def printBoard(self):
    for y in range(0,9):
      string =''
      for x in range(0,9):
        if self.board[y][x].value == 0:
          string += ' '
        else:
          string += ' ' + str(self.board[y][x].value)
      print(string)

  #resets the board, taking in a csv file
  def clear(self, file_name):
    #reads in data
    self.board = []
    vals = pd.read_csv(file_name)
    vals_length = int(vals.count())
    counter = 0
    #reassigns the values in the board
    for x in range(0,9): 
      row=[]
      for y in range(0,9):
        val = vals['b'][counter]
        isPlay = vals['b'][counter+1]
        row.append(Cell(val,isPlay))
        counter += 2
      self.board.append(row)
      return True

  #loads a previously saved game from a csv
  def load(self, file_name):
    #checks if the csv exists
    self.board = []
    if not os.path.isfile(file_name):
      return False
    vals = pd.read_csv(file_name)
    vals_length = vals.count().astype(int)
    counter = 0
    #resets the values
    for x in range(0,9): 
      row=[]
      for y in range(0,9):
        val = vals['b'][counter]
        isPlay = vals['b'][counter+1]
        row.append(Cell(val,isPlay))
        counter += 2
      self.board.append(row)
    return True
  
  #saves a current game to a specified csv
  def save(self, file_name):
    vals = []
    #gets values from the board
    for x in range(0,9): 
      for y in range(0,9):
        val = self.board[x][y].value
        isPlay = self.board[x][y].isPlayable
        if isPlay == "FALSE":
          isPlay = False
        else:
          isPlay = True
        
        vals.append(val)
        vals.append(isPlay)
    #writes the values to the board
    df = pd.DataFrame(vals)
    df.columns = ['b']
    df.to_csv(file_name)
    return True
  
  #checks to see if the board is valid horizontally
  def isValidHorz(self):
    s = set()
    for y in range(0,9):
      for x in range(0,9):
        #if a number isnt valid
        if int(self.board[x][y].value) > 9 or int(self.board[x][y].value) < 1 or s.add(self.board[x][y].value) == False:
          print(self.board[x][y].value + " is the value")
          print("horz fail at" + str(x) + " " + str(y))
          return False
      s.clear()
    return True

  #checks to see if the columns of the board are valid
  def isValidVert(self):
    s = set()
    for x in range(0,9):
      for y in range(0,9):
        #if an invalid case
        if int(self.board[x][y].value) > 9 or int(self.board[x][y].value) < 1 or s.add(self.board[x][y].value) == False:
          return False
      s.clear()
    return True

  #checks to see if each box is valid
  def isValidBox(self):
    s = set()
    #upper left box
    for x in range(0,3):
      for y in range(0,3):
        if int(self.board[x][y].value) > 9 or int(self.board[x][y].value) < 1 or s.add(self.board[x][y].value) == False:
          return False
    s.clear()

    #upper middle box
    for x in range(3,6):
        for y in range(0,3):
            if int(self.board[x][y].value) > 9 or int(self.board[x][y].value) < 1 or s.add(self.board[x][y].value) == False:
                return False
    s.clear()

    #upper right box
    for x in range(6,9):
        for y in range(0,3):
            if int(self.board[y][x].value) > 9 or int(self.board[y][x].value) < 1 or s.add(self.board[y][x].value) == False:
                return False
    s.clear()

    #middle left box
    for x in range(0,3):
        for y in range(3,6):
            if int(self.board[y][x].value) > 9 or int(self.board[y][x].value) < 1 or s.add(self.board[y][x].value) == False:
                return False
    s.clear()

    #middle middle box
    for x in range(3,6):
        for y in range(3,6):
            if int(self.board[y][x].value) > 9 or int(self.board[y][x].value) < 1 or s.add(self.board[y][x].value) == False:
                return False
    s.clear()

    #middle right box
    for x in range(6,9):
        for y in range(3,6):
            if int(self.board[y][x].value) > 9 or int(self.board[y][x].value) < 1 or s.add(self.board[y][x].value) == False:
                return False
    s.clear()

    #bottom left box
    for x in range(0,3):
        for y in range(6,9):
            if int(self.board[y][x].value) > 9 or int(self.board[y][x].value) < 1 or s.add(self.board[y][x].value) == False:
                return False
    s.clear()

    #bottom middle box
    for x in range(3,6):
        for y in range(6,9):
            if int(self.board[y][x].value) > 9 or int(self.board[y][x].value) < 1 or s.add(self.board[y][x].value) == False:
                return False
    s.clear()

    #bottom right box
    for x in range(6,9):
        for y in range(6,9):
            if int(self.board[y][x].value) > 9 or int(self.board[y][x].value) < 1 or s.add(self.board[y][x].value) == False:
                return False
    s.clear()

    return True

    #returns true if the sudoku board is a valid solution
  def isCorrect(self):
    return self.isValidBox() and self.isValidHorz() and self.isValidVert()


