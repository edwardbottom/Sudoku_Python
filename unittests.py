import unittest
from Board import Board


class EndGameTest(unittest.TestCase):
	failBoard = Board()
	#failBoard.load('fail_board.csv')
	successBoard = Board()
	#successBoard.load('success_board.csv')
	
	def test_is_horiz_fail(self):
		self.assertFalse(self.failBoard.isValidHoriz())

	def test_is_vert_fail(self):
		self.assertFalse(self.failBoard.isValidVert())

	def test_is_box_fail(self):
		self.assertFalse(self.failBoard.isValidBox())
	
	def test_is_horiz_success(self):
		self.assertTrue(self.successBoard.isValidHoriz())

	def test_is_vert_success(self):
		self.assertTrue(self.successBoard.isValidVert())

	def test_is_box_success(self):
		self.assertTrue(self.successBoard.isValidBox())

	def test_clear_is_working(self):
		self.assertTrue(self.failBoard.clear())

	def test_save_is_working(self):
		self.assertTrue(self.failBoard.save("save.csv"))

	def test_load_is_working(self):
		self.assertTrue(self.failBoard.load())


if __name__ == '__main__':
    unittest.main()