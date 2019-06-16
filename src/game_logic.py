from piece_type import GAME_PIECE_X, GAME_PIECE_O, BLANK_PIECE
import random

#            0          1          2          3         4          5          6          7
paths = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],[1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

paths_at_index = [[0, 3, 6], [0, 4], [0, 5, 7], [1, 3],[1, 4, 6, 7], [1, 5], [2, 3, 7], [2, 4], [2, 5, 6]]


def analyze_path(count, playerPiece):

    if count[0] == 0:                      # full path
        return 0

    if count[0] == 3:                      # empty path
        return 1

    if count[1] == 1 and count[2] == 1:
        return 0

    if count[1] == 2:                      # immediate win
        return 100

    if count[2] == 2:                      # immediate block
        return 25

    if count[1] == 1 and count[2] == 0:    # potential win
        if playerPiece == GAME_PIECE_X:
            return 10
        else:
            return 5

    if count[1] == 0 and count[2] == 1:    # potential block
        if playerPiece == GAME_PIECE_O:
            return 5
        else:
            return 10


# Scans game board and tallies all the X, O, and Blanks given a path
def calc_piece_count(path, gameboard):
    piece_counts = [0] * 3

    for index in path:
        piece = gameboard[index]
        if piece == BLANK_PIECE:
            piece_counts[0] += 1
        elif piece == GAME_PIECE_X:
            piece_counts[1] += 1
        else:
            piece_counts[2] += 1
    return piece_counts

# calculates the weight for all game paths


def update_path_weights(gameboard, playerPiece):
    global paths

    # calculate each path's weight based on piece counts
    path_weights = []
    for path in paths:
        piece_count = calc_piece_count(path, gameboard)
        weight = analyze_path(piece_count, playerPiece)
        path_weights.append(weight)

    return path_weights

# based on the number of paths at a given position, tallies the weights


def update_position_weights(path_weights, gameboard):
    global paths_at_index
    position_weights = [0] * 9

    # adds path weights for a given position
    for i in range(len(paths_at_index)):
        if gameboard[i] != BLANK_PIECE:
            weight_at_index = -1
        else:
            paths = paths_at_index[i]
            weight_at_index = 0
            for path in paths:
                weight_at_index += path_weights[path]

        position_weights[i] = weight_at_index

    return position_weights

def choose_path(weights_at_index) :
    # pick the best index
    GameOver = False
    best_indices = []
    best_weight = max(weights_at_index)

    if (best_weight < 0) :
        return -1

    while (max(weights_at_index) == best_weight) :
        best_index = weights_at_index.index(max(weights_at_index))
        best_indices.append(best_index)
        weights_at_index[best_index] = -1
    
    return random.choice(best_indices), GameOver

def check_gameOver(gameboard, playerPiece):
    global paths
    blank_count = 0

    for path in paths:
        piece_count = calc_piece_count(path, gameboard)
        if (piece_count[1] == 3 or piece_count[2] == 3) :
            return True, True
        blank_count += piece_count[0]

    if (blank_count == 0) : 
        return True, False

    return False, False