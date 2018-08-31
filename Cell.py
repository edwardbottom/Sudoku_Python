class Cell:
  def __init__(self, value, isPlayable):
    self.value = value
    self.isPlayable = isPlayable

  def isPlayable(self):
  	return self.isPlayable

  def getValue(self):
  	return self.value

  def setValue(self, val):
  	if(self.isPlayable):
  		self.value = val
  		return True
  	else:
  		return False
  	





