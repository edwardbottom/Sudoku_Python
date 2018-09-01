#class for a cell object that tracks the cell's value 
#and playability
class Cell:
  #construcotr for the cell that takes in a value and
  #a boolean that indicates the playability of the cell
  def __init__(self, value, isPlayable):
    self.value = value
    self.isPlayable = isPlayable

  #returns a boolean for if the cell is playable or not
  def isPlayable(self):
  	return self.isPlayable

  #gets the value of the cell
  def getValue(self):
  	return self.value

  #sets the value of the cell to a specified in between 1-9
  #if the cell is playable
  def setValue(self, val):
    #if a valid move
  	if(self.isPlayable and int(val) > 0 and int(val) < 10):
  		self.value = val
  		return True
    #if an invalid move
  	else:
  		return False
  	





