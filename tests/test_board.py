from board import Board
from fen import Fen


def make_pawn_board() -> Board:
    # Mixed board for helper-method tests
    board = Board()
    Fen.load("8/1p2P3/8/3p2P1/1P6/5p2/3P4/8", board)
    return board


def test_verify_source_and_destination_valid_black_piece() -> None:
    # Black piece to empty square
    board = make_pawn_board()
    assert board.verify_source_and_destination(1, 1, 2, 1, True)


def test_verify_source_and_destination_valid_white_piece() -> None:
    # White piece to empty square
    board = make_pawn_board()
    assert board.verify_source_and_destination(1, 4, 0, 4, False)


def test_verify_source_and_destination_wrong_turn_color() -> None:
    # Wrong player turn
    board = make_pawn_board()
    assert not board.verify_source_and_destination(1, 1, 2, 1, False)


def test_verify_source_and_destination_out_of_bounds() -> None:
    # Source out of bounds
    board = make_pawn_board()
    assert not board.verify_source_and_destination(-1, 1, 2, 1, True)


def test_verify_source_and_destination_end_out_of_bounds() -> None:
    # Destination out of bounds
    board = make_pawn_board()
    assert not board.verify_source_and_destination(1, 1, 8, 1, True)


def test_verify_source_and_destination_empty_source() -> None:
    # Empty source square
    board = make_pawn_board()
    assert not board.verify_source_and_destination(0, 0, 2, 1, True)


def test_verify_source_and_destination_same_color_destination() -> None:
    # Cannot move onto own piece
    board = make_pawn_board()
    assert not board.verify_source_and_destination(1, 4, 3, 6, False)


def test_verify_source_and_destination_opponent_destination() -> None:
    # Can move onto opponent piece
    board = make_pawn_board()
    assert board.verify_source_and_destination(1, 4, 3, 3, False)



def test_verify_horizontal_clear_path() -> None:
    # Clear horizontal path
    board = Board()
    board.clear()
    assert board.verify_horizontal(4, 1, 4, 7)


def test_verify_horizontal_blocked_path() -> None:
    # Blocked horizontal path
    board = make_pawn_board()
    assert not board.verify_horizontal(1, 1, 1, 7)


def test_verify_horizontal_wrong_row() -> None:
    # Not horizontal
    board = Board()
    board.clear()
    assert not board.verify_horizontal(1, 1, 4, 1)


def test_verify_vertical_clear_path() -> None:
    # Clear vertical path
    board = Board()
    board.clear()
    assert board.verify_vertical(1, 4, 7, 4)


def test_verify_vertical_blocked_path() -> None:
    # Blocked vertical path
    board = make_pawn_board()
    assert not board.verify_vertical(1, 1, 7, 1)


def test_verify_vertical_wrong_col() -> None:
    # Not vertical
    board = Board()
    board.clear()
    assert not board.verify_vertical(1, 1, 1, 4)


def test_verify_diagonal_clear_path() -> None:
    # Clear diagonal path
    board = Board()
    board.clear()
    assert board.verify_diagonal(1, 1, 6, 6)


def test_verify_diagonal_blocked_path() -> None:
    # Blocked diagonal path
    board = make_pawn_board()
    assert not board.verify_diagonal(1, 1, 5, 5)


def test_verify_diagonal_not_diagonal() -> None:
    # Not diagonal
    board = Board()
    board.clear()
    assert not board.verify_diagonal(1, 1, 4, 5)


def test_verify_adjacent_diagonal_neighbor() -> None:
    # One square diagonally
    board = Board()
    assert board.verify_adjacent(4, 4, 5, 5)


def test_verify_adjacent_same_square() -> None:
    # Same square allowed by helper
    board = Board()
    assert board.verify_adjacent(4, 4, 4, 4)


def test_verify_adjacent_non_neighbor() -> None:
    # More than one square away
    board = Board()
    assert not board.verify_adjacent(4, 4, 6, 4)


def test_verify_adjacent_horizontal_neighbor() -> None:
    # One square horizontally
    board = Board()
    assert board.verify_adjacent(4, 4, 4, 5)


def test_verify_adjacent_vertical_neighbor() -> None:
    # One square vertically
    board = Board()
    assert board.verify_adjacent(4, 4, 5, 4)