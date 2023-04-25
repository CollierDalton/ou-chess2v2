import unittest
from chess_engine import game_state

#board = game_state.__init__
#board = game_state()

class TestChessBoard(unittest.TestCase):
    #board = game_state()
    #white_pieces = board.white_pieces
    #black_pieces = board.black_pieces

    def test_white_king_location(self):
        board = game_state()
        self.assertEqual(board._white_king_location, [0, 4])

    def test_black_king_location(self):
        board = game_state()
        self.assertEqual(board._black_king_location, [8, 4])

    def test_numOf_white_pieces(self):
        board = game_state()
        white_pieces = board.white_pieces
        self.assertEqual(len(white_pieces), 18)

    def test_numOf_black_pieces(self):
        board = game_state()
        black_pieces = board.black_pieces
        self.assertEqual(len(black_pieces), 18)

if __name__ == '__main__':
    unittest.main()