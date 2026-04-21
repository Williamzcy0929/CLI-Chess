"""Test for the Knight class."""

from src.board import Board
from src.piece import Piece

def test_knight_move_legal() -> None:
    """Test knight legal L-shape moves."""
    board = Board()
    board.clear()
    knight = Piece("\u2658", 2, 2, False)
    board.set_piece(2, 2, knight)
    assert knight.is_move_legal(board, 3, 4)
    assert knight.is_move_legal(board, 4, 3)


def test_knight_move_illegal_when_not_l_shape() -> None:
    """Test knight cannot move in non-L patterns."""
    board = Board()
    board.clear()
    knight = Piece("\u2658", 2, 2, False)
    board.set_piece(2, 2, knight)
    assert not knight.is_move_legal(board, 2, 5)
    assert not knight.is_move_legal(board, 3, 3)
    assert not knight.is_move_legal(board, 1, 1)


def test_knight_capture_enemy_piece() -> None:
    """Test knight can capture an enemy piece on legal destination."""
    board = Board()
    board.clear()
    knight = Piece("\u2658", 2, 2, False)
    enemy = Piece("\u265f", 3, 4, True)
    board.set_piece(2, 2, knight)
    board.set_piece(3, 4, enemy)

    assert knight.is_move_legal(board, 3, 4)


def test_knight_cannot_capture_own_piece() -> None:
    """Test knight cannot capture a piece of same color."""
    board = Board()
    board.clear()
    knight = Piece("\u2658", 2, 2, False)
    ally = Piece("\u2659", 3, 4, False)
    board.set_piece(2, 2, knight)
    board.set_piece(3, 4, ally)

    assert not knight.is_move_legal(board, 3, 4)


def test_knight_can_jump_over_blocking_piece() -> None:
    """Test knight movement is not blocked by intervening piece."""
    board = Board()
    board.clear()
    knight = Piece("\u2658", 2, 2, False)
    blocker = Piece("\u2659", 2, 3, False)
    board.set_piece(2, 2, knight)
    board.set_piece(2, 3, blocker)

    assert knight.is_move_legal(board, 3, 4)