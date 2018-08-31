import unittest
from Board import Board


class EndGameTest(unittest.TestCase):
	testBoard = Board()
	
	def test_is_horiz_correct(self):
		self.assertFalse(self.testBoard.isValidHoriz())

	def test_is_vert_correct(self):
		self.assertFalse(self.testBoard.isValidVert())

	def test_is_box_correct(self):
		self.assertFalse(self.testBoard.isValidBox())


if __name__ == '__main__':
    unittest.main()