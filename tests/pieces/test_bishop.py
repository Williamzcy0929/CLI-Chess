"""Test for the Bishop class."""

from board import Board
from piece import Piece


def test_bishop_diagonal_movement() -> None:
    """Test legal and illegal diagonal movement only."""
    board = Board()
    board.clear()
    bishop = Piece("\u2657", 2, 2, False)
    board.set_piece(2, 2, bishop)

    assert bishop.is_move_legal(board, 0, 0)
    assert bishop.is_move_legal(board, 5, 5)
    assert not bishop.is_move_legal(board, 2, 5)


def test_bishop_capture_enemy_piece() -> None:
    """Test bishop can capture an enemy piece on diagonal."""
    board = Board()
    board.clear()
    bishop = Piece("\u2657", 2, 2, False)
    enemy = Piece("\u265f", 5, 5, True)
    board.set_piece(2, 2, bishop)
    board.set_piece(5, 5, enemy)

    assert bishop.is_move_legal(board, 5, 5)


def test_bishop_cannot_capture_own_piece() -> None:
    """Test bishop cannot capture a piece of same color."""
    board = Board()
    board.clear()
    bishop = Piece("\u2657", 2, 2, False)
    ally = Piece("\u2659", 5, 5, False)
    board.set_piece(2, 2, bishop)
    board.set_piece(5, 5, ally)

    assert not bishop.is_move_legal(board, 5, 5)


def test_bishop_blocked_path() -> None:
    """Test bishop cannot move through blocking piece."""
    board = Board()
    board.clear()
    bishop = Piece("\u2657", 2, 2, False)
    blocker = Piece("\u2659", 3, 3, False)
    board.set_piece(2, 2, bishop)
    board.set_piece(3, 3, blocker)

    assert not bishop.is_move_legal(board, 5, 5)