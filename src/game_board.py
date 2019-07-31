from piece_type import GAME_PIECE_X, GAME_PIECE_O, BLANK_PIECE


class GameBoard(object):

    # This is a simple comment line
    game_board = []

    def __init__(self):
        #print("Creating GameBoard Class")
        pass

    def create_board(self):
        self.game_board = [BLANK_PIECE] * 9

    def get_board(self):
        return self.game_board

    def print_board(self):

        print(
            f"{self.game_board[0]} | {self.game_board[1]} | {self.game_board[2]}")
        print(
            f"{self.game_board[3]} | {self.game_board[4]} | {self.game_board[5]}")
        print(
            f"{self.game_board[6]} | {self.game_board[7]} | {self.game_board[8]}")

    def put_piece(self, index, pieceType):
        self.game_board[index] = pieceType

    def get_piece(self, index):
        return self.game_board[index]
