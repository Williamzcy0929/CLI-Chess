"""Tests for board helper validation methods."""

from board import Board
from fen import Fen


def make_pawn_board() -> Board:
    """Create a mixed board position for helper-method tests."""
    board = Board()
    Fen.load("8/1p2P3/8/3p2P1/1P6/5p2/3P4/8", board)
    return board

def test_verify_source_and_destination_valid_black_piece() -> None:
    """Allow valid black source and destination."""
    board = make_pawn_board()
    assert board.verify_source_and_destination(1, 1, 2, 1, True)


def test_verify_source_and_destination_valid_white_piece() -> None:
    """Allow valid white source and destination."""
    board = make_pawn_board()
    assert board.verify_source_and_destination(1, 4, 0, 4, False)


def test_verify_source_and_destination_wrong_turn_color() -> None:
    """Reject source piece that does not match active color."""
    board = make_pawn_board()
    assert not board.verify_source_and_destination(1, 1, 2, 1, False)


def test_verify_source_and_destination_out_of_bounds() -> None:
    """Reject source coordinates outside board bounds."""
    board = make_pawn_board()
    assert not board.verify_source_and_destination(-1, 1, 2, 1, True)


def test_verify_source_and_destination_end_out_of_bounds() -> None:
    """Reject destination coordinates outside board bounds."""
    board = make_pawn_board()
    assert not board.verify_source_and_destination(1, 1, 8, 1, True)


def test_verify_source_and_destination_empty_source() -> None:
    """Reject moves from empty source squares."""
    board = make_pawn_board()
    assert not board.verify_source_and_destination(0, 0, 2, 1, True)


def test_verify_source_and_destination_same_color_destination() -> None:
    """Reject moves to a destination occupied by same color."""
    board = make_pawn_board()
    assert not board.verify_source_and_destination(1, 4, 3, 6, False)


def test_verify_source_and_destination_opponent_destination() -> None:
    """Allow moves to a destination occupied by opponent."""
    board = make_pawn_board()
    assert board.verify_source_and_destination(1, 4, 3, 3, False)



def test_verify_horizontal_clear_path() -> None:
    """Return true for clear horizontal paths."""
    board = Board()
    board.clear()
    assert board.verify_horizontal(4, 1, 4, 7)


def test_verify_horizontal_blocked_path() -> None:
    """Return false for blocked horizontal paths."""
    board = make_pawn_board()
    assert not board.verify_horizontal(1, 1, 1, 7)


def test_verify_horizontal_wrong_row() -> None:
    """Return false when row changes during horizontal check."""
    board = Board()
    board.clear()
    assert not board.verify_horizontal(1, 1, 4, 1)


def test_verify_vertical_clear_path() -> None:
    """Return true for clear vertical paths."""
    board = Board()
    board.clear()
    assert board.verify_vertical(1, 4, 7, 4)


def test_verify_vertical_blocked_path() -> None:
    """Return false for blocked vertical paths."""
    board = make_pawn_board()
    assert not board.verify_vertical(1, 1, 7, 1)


def test_verify_vertical_wrong_col() -> None:
    """Return false when column changes during vertical check."""
    board = Board()
    board.clear()
    assert not board.verify_vertical(1, 1, 1, 4)


def test_verify_diagonal_clear_path() -> None:
    """Return true for clear diagonal paths."""
    board = Board()
    board.clear()
    assert board.verify_diagonal(1, 1, 6, 6)


def test_verify_diagonal_blocked_path() -> None:
    """Return false for blocked diagonal paths."""
    board = make_pawn_board()
    assert not board.verify_diagonal(1, 1, 5, 5)


def test_verify_diagonal_not_diagonal() -> None:
    """Return false for non-diagonal movement pairs."""
    board = Board()
    board.clear()
    assert not board.verify_diagonal(1, 1, 4, 5)


def test_verify_adjacent_diagonal_neighbor() -> None:
    """Return true for diagonal neighbor squares."""
    board = Board()
    assert board.verify_adjacent(4, 4, 5, 5)


def test_verify_adjacent_same_square() -> None:
    """Return true for identical source and destination squares."""
    board = Board()
    assert board.verify_adjacent(4, 4, 4, 4)


def test_verify_adjacent_non_neighbor() -> None:
    """Return false for non-adjacent squares."""
    board = Board()
    assert not board.verify_adjacent(4, 4, 6, 4)


def test_verify_adjacent_horizontal_neighbor() -> None:
    """Return true for horizontal neighbor squares."""
    board = Board()
    assert board.verify_adjacent(4, 4, 4, 5)


def test_verify_adjacent_vertical_neighbor() -> None:
    """Return true for vertical neighbor squares."""
    board = Board()
    assert board.verify_adjacent(4, 4, 5, 4)