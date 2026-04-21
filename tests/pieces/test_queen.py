"""Test for the Queen class."""

from board import Board
from piece import Piece


def test_queen_movement_directions() -> None:
    """Test queen legal moves in three directions."""
    board = Board()
    board.clear()
    queen = Piece("\u2655", 4, 4, False)
    board.set_piece(4, 4, queen)

    assert queen.is_move_legal(board, 4, 1)
    assert queen.is_move_legal(board, 1, 4)
    assert queen.is_move_legal(board, 1, 1)


def test_queen_move_illegal_when_not_straight_or_diagonal() -> None:
    """Test queen cannot move in non-linear patterns."""
    board = Board()
    board.clear()
    queen = Piece("\u2655", 4, 4, False)
    board.set_piece(4, 4, queen)

    assert not queen.is_move_legal(board, 2, 3)
    assert not queen.is_move_legal(board, 5, 2)


def test_queen_capture_enemy_piece() -> None:
    """Test queen can capture enemy on legal path."""
    board = Board()
    board.clear()
    queen = Piece("\u2655", 4, 4, False)
    enemy = Piece("\u265f", 4, 7, True)
    board.set_piece(4, 4, queen)
    board.set_piece(4, 7, enemy)

    assert queen.is_move_legal(board, 4, 7)


def test_queen_cannot_capture_own_piece() -> None:
    """Test queen cannot capture same-color piece."""
    board = Board()
    board.clear()
    queen = Piece("\u2655", 4, 4, False)
    ally = Piece("\u2659", 1, 1, False)
    board.set_piece(4, 4, queen)
    board.set_piece(1, 1, ally)

    assert not queen.is_move_legal(board, 1, 1)


def test_queen_blocked_path() -> None:
    """Test queen cannot move through blocking piece."""
    board = Board()
    board.clear()
    queen = Piece("\u2655", 4, 4, False)
    blocker = Piece("\u2659", 4, 5, False)
    board.set_piece(4, 4, queen)
    board.set_piece(4, 5, blocker)

    assert not queen.is_move_legal(board, 4, 7)
