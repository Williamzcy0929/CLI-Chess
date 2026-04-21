"""Test for the Rook class."""

from src.board import Board
from src.piece import Piece


def test_rook_horizontal_and_vertical_movement() -> None:
    """Test rook legal movement in straight lines."""
    board = Board()
    board.clear()
    rook = Piece("\u2656", 4, 4, False)
    board.set_piece(4, 4, rook)

    assert rook.is_move_legal(board, 4, 1)
    assert rook.is_move_legal(board, 1, 4)


def test_rook_move_illegal_when_not_straight_line() -> None:
    """Test rook cannot move diagonally."""
    board = Board()
    board.clear()
    rook = Piece("\u2656", 4, 4, False)
    board.set_piece(4, 4, rook)

    assert not rook.is_move_legal(board, 3, 3)
    assert not rook.is_move_legal(board, 2, 1)


def test_rook_capture_enemy_piece() -> None:
    """Test rook can capture enemy on clear path."""
    board = Board()
    board.clear()
    rook = Piece("\u2656", 4, 4, False)
    enemy = Piece("\u265f", 4, 7, True)
    board.set_piece(4, 4, rook)
    board.set_piece(4, 7, enemy)

    assert rook.is_move_legal(board, 4, 7)


def test_rook_cannot_capture_own_piece() -> None:
    """Test rook cannot capture same-color piece."""
    board = Board()
    board.clear()
    rook = Piece("\u2656", 4, 4, False)
    ally = Piece("\u2659", 4, 7, False)
    board.set_piece(4, 4, rook)
    board.set_piece(4, 7, ally)

    assert not rook.is_move_legal(board, 4, 7)


def test_rook_blocked_path() -> None:
    """Test rook cannot move through an intervening piece."""
    board = Board()
    board.clear()
    rook = Piece("\u2656", 4, 4, False)
    blocker = Piece("\u2659", 4, 5, False)
    board.set_piece(4, 4, rook)
    board.set_piece(4, 5, blocker)

    assert not rook.is_move_legal(board, 4, 7)
