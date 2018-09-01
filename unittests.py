import unittest
from Board import Board


class EndGameTest(unittest.TestCase):
	failBoard = Board("test_board_false.csv")
	successBoard = Board("completed_game.csv")

	
	def test_is_horiz_fail(self):
		self.assertFalse(self.failBoard.isValidHorz())

	def test_is_vert_fail(self):
		self.assertFalse(self.failBoard.isValidVert())

	def test_is_box_fail(self):
		self.assertFalse(self.failBoard.isValidBox())
	
	def test_is_horiz_success(self):
		self.assertTrue(self.successBoard.isValidHorz())

	def test_is_vert_success(self):
		self.assertTrue(self.successBoard.isValidVert())

	def test_is_box_success(self):
		self.assertTrue(self.successBoard.isValidBox())

	def test_clear_is_working(self):
		self.assertTrue(self.failBoard.clear("test_board_false.csv"))

	def test_save_is_working(self):
		self.assertTrue(self.failBoard.save("save.csv"))

	def test_load_is_working(self):
		self.assertTrue(self.failBoard.load("test_board_false.csv"))


if __name__ == '__main__':
    unittest.main()