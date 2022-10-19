import unittest
from game import inLine

class TestInLine(unittest.TestCase):
    def test_board(self):
        game = inLine()
        self.assertEqual(len(game.board),6)
        self.assertEqual(len(game.board[0]),7)

    def test_available(self):
        game = inLine()
        game.available(1)
        game.board = [[0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0]]
        self.assertEqual(game.available(0),0)

    def test_throw_coin(self):
        game = inLine()
        game.throw_coin(1)
        self.assertEqual(game.board[5][1],1)

    def test_change_turn(self):
        game = inLine()
        game.change_turn()
        self.assertEqual(game.player,2)

    def test_change_turn2(self):
        game = inLine()
        game.player = 2
        game.change_turn()
        self.assertEqual(game.player,1)


    def test_check_row(self):
        game = inLine()
        game.check_row()
        game.board = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [2, 2, 2, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0]]
        self.assertEqual(game.check_row(),True)

    def test_check_row2(self):
        game = inLine()
        game.check_row()
        game.board = [[1, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 1]]
        self.assertEqual(game.check_row(),None)

    def test_check_col(self):
        game = inLine()
        game.check_col()
        game.board = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 1]]
        self.assertEqual(game.check_col(),True)

    def test_check_col2(self):
        game = inLine()
        game.check_col()
        game.board = [[0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
        self.assertEqual(game.check_col(),None)

    def test_check_diag(self):
        game = inLine()
        game.check_diag()
        game.board = [[1, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 1]]
        self.assertEqual(game.check_diag(),None)

    def test_check_diag2(self):
        game = inLine()
        game.check_diag()
        game.board = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0]]        
        self.assertEqual(game.check_diag(),True)

    def test_check_diag_inverse(self):
        game = inLine()
        game.check_diag_inverse()
        game.board = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0]]
        self.assertEqual(game.check_diag_inverse(),None)

    def test_check_diag_inverse(self):
        game = inLine()
        game.check_diag_inverse()
        game.board = [[0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0]]
        self.assertEqual(game.check_diag_inverse(),True)

    def test_check_winner(self):
        game = inLine()
        game.check_winner()
        game.board = [[1, 1, 1, 1, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
        self.assertEqual(game.check_winner(),True)

    









if __name__ == '__main__':
    unittest.main()