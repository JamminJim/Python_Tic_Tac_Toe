import time
import os
import timeit

from game_board import GameBoard
from game_logic import update_path_weights, update_position_weights, choose_path, check_gameOver
from submodule.piece_type import GAME_PIECE_O, GAME_PIECE_X


def run_game():

    # create the game board
    gameboard = GameBoard()

    GameOver = False

    # create game board
    gameboard.create_board()

    # set player piece type
    player = GAME_PIECE_X

    while GameOver == False:

        # update weights for each possible path
        path_weights = update_path_weights(gameboard.get_board(), player)

        # tallies weights at each board position
        position_weights = update_position_weights(
            path_weights, gameboard.get_board())

        # chooses best position based on weights
        best_position, GameOver = choose_path(position_weights)

        #print(f"Best Pos {best_position}")
        # time.sleep(1)

        # mark position on board
        gameboard.put_piece(best_position, player)

        # update game board
        # gameboard.print_board()

        # check if game is over
        GameOver, isWinner = check_gameOver(gameboard.get_board(), player)

        if (GameOver == False and isWinner == False):
            # switch player
            if player == GAME_PIECE_X:
                player = GAME_PIECE_O
            else:
                player = GAME_PIECE_X

        # wait one second between turns
        # time.sleep(1)


if __name__ == '__main__':
    print(timeit.timeit("run_game()",
                        setup="from __main__ import run_game", number=10000))


#print(f"Path Weights : {path_weights}")
#print(f"Position Weights : {position_weights}")
#print(f"Best Position : {best_position}")
#print(f"Is Winner?: {winner}")
