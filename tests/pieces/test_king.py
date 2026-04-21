"""Test for the King class."""

from board import Board
from piece import Piece


def test_king_move_legal() -> None:
    """Test king moves one square in any direction."""
    board = Board()
    board.clear()
    king = Piece("\u2654", 2, 2, False)
    board.set_piece(2, 2, king)
    assert king.is_move_legal(board, 2, 3)
    assert king.is_move_legal(board, 3, 2)
    assert king.is_move_legal(board, 3, 3)


def test_king_move_illegal_when_not_adjacent() -> None:
    """Test king cannot move more than one square."""
    board = Board()
    board.clear()
    king = Piece("\u2654", 2, 2, False)
    board.set_piece(2, 2, king)
    assert not king.is_move_legal(board, 2, 4)
    assert not king.is_move_legal(board, 4, 2)
    assert not king.is_move_legal(board, 4, 4)

def test_king_capture_enemy_piece() -> None:
    """Test king can capture an enemy piece on adjacent."""
    board = Board()
    board.clear()
    king = Piece("\u2654", 2, 2, False)
    enemy = Piece("\u265f", 3, 3, True)
    board.set_piece(2, 2, king)
    board.set_piece(3, 3, enemy)

    assert king.is_move_legal(board, 3, 3)


def test_king_cannot_capture_own_piece() -> None:
    """Test king cannot capture a piece of same color."""
    board = Board()
    board.clear()
    king = Piece("\u2654", 2, 2, False)
    ally = Piece("\u2659", 3, 3, False)
    board.set_piece(2, 2, king)
    board.set_piece(3, 3, ally)

    assert not king.is_move_legal(board, 3, 3)

def test_king_blocked_path() -> None:
    """Test king move remains illegal for distant destination."""
    board = Board()
    board.clear()
    king = Piece("\u2654", 2, 2, False)
    blocker = Piece("\u2659", 3, 3, False)
    board.set_piece(2, 2, king)
    board.set_piece(3, 3, blocker)

    assert not king.is_move_legal(board, 5, 5)