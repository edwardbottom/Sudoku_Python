from Cell import Cell
import pandas as pd
import os

class Board:
  def __init__(self, file_name):
    self.board = []
    vals = pd.read_csv(file_name)
    vals_length = vals.count().astype(int)
    counter = 0
    for x in range(0,9): 
      row=[]
      for y in range(0,9):
        val = vals['b'][counter]
        isPlay = vals['b'][counter+1]
        # val = int(str(vals.values[(counter)]).strip("[]").strip("''"))
        row.append(Cell(val,isPlay))
        counter += 2
      self.board.append(row)

  def printBoard(self):
    for y in range(0,9):
      string =''
      for x in range(0,9):
        if self.board[y][x].value == 0:
          string += ' '
        else:
          string += ' ' + str(self.board[y][x].value)
      print(string)

  def clear(self, file_name):
    self.board = []
    vals = pd.read_csv(file_name)
    vals_length = int(vals.count())
    counter = 0
    for x in range(0,9): 
      row=[]
      for y in range(0,9):
        val = vals['b'][counter]
        isPlay = vals['b'][counter+1]
        row.append(Cell(val,isPlay))
        counter += 2
      self.board.append(row)
      return True

  def load(self, file_name):
    self.board = []
    if not os.path.isfile(file_name):
      return False
    vals = pd.read_csv(file_name)
    vals_length = vals.count().astype(int)
    counter = 0
    for x in range(0,9): 
      row=[]
      for y in range(0,9):
        # val = int(str(vals.values[(counter)]).strip("[]").strip("''"))
        val = vals['b'][counter]
        isPlay = vals['b'][counter+1]
        row.append(Cell(val,isPlay))
        counter += 2
      self.board.append(row)
    return True
  
  def save(self, file_name):
    vals = []
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
    df = pd.DataFrame(vals)
    df.columns = ['b']
    df.to_csv(file_name)
    return True
  
  def isValidHorz(self):
    s = set()
    for y in range(0,9):
      for x in range(0,9):
        if int(self.board[x][y].value) > 9 or int(self.board[x][y].value) < 1 or not s.add(self.board[x][y].value):
          return False
      s.clear()
    return True

  def isValidVert(self):
    s = set()
    for x in range(0,9):
        for y in range(0,9):
            if int(self.board[x][y].value) > 9 or int(self.board[x][y].value) < 1 or not s.add(self.board[x][y].value):
                return False
        s.clear()
    return True

  def isValidBox(self):
    s = set()
    #upper left box
    for x in range(0,3):
        for y in range(0,3):
            if int(self.board[y][x].value) > 9 or int(self.board[y][x].value) < 1 or not s.add(self.board[y][x].value):
                return False
    s.clear()

    #upper middle box
    for x in range(3,6):
        for y in range(0,3):
            if int(self.board[y][x].value) > 9 or int(self.board[y][x].value) < 1 or not s.add(self.board[y][x].value):
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
            if int(self.board[y][x].value) > 9 or int(self.board[y][x].value) < 1 or not s.add(self.board[y][x].value):
                return False
    s.clear()

    #middle middle box
    for x in range(3,6):
        for y in range(3,6):
            if int(self.board[y][x].value) > 9 or int(self.board[y][x].value) < 1 or not s.add(self.board[y][x].value):
                return False
    s.clear()

    #middle right box
    for x in range(6,9):
        for y in range(3,6):
            if int(self.board[y][x].value) > 9 or int(self.board[y][x].value) < 1 or not s.add(self.board[y][x].value):
                return False
    s.clear()

    #bottom left box
    for x in range(0,3):
        for y in range(6,9):
            if int(self.board[y][x].value) > 9 or int(self.board[y][x].value) < 1 or not s.add(self.board[y][x].value):
                return False
    s.clear()

    #bottom middle box
    for x in range(3,6):
        for y in range(6,9):
            if int(self.board[y][x].value) > 9 or int(self.board[y][x].value) < 1 or not set.add(self.board[y][x].value):
                return False
    set.clear()

    #bottom right box
    for x in range(6,9):
        for y in range(6,9):
            if int(self.board[y][x].value) > 9 or int(self.board[y][x].value) < 1 or not s.add(self.board[y][x].value):
                return False
    s.clear()

    return True

  def isCorrect(self):
    return self.isValidBox() and self.isValidHorz() and self.isValidVert()





