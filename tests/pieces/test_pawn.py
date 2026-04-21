"""Test for the Pawn class."""

from src.board import Board
from src.piece import Piece


def test_pawn_move_one_step_forward() -> None:
    """Test pawn moves one square forward into empty space."""
    board = Board()
    board.clear()
    pawn = Piece("\u2659", 6, 3, False)
    board.set_piece(6, 3, pawn)
    assert pawn.is_move_legal(board, 5, 3)


def test_pawn_move_two_steps_from_start() -> None:
    """Test pawn can move two squares from its starting row."""
    board = Board()
    board.clear()
    pawn = Piece("\u2659", 6, 3, False)
    board.set_piece(6, 3, pawn)
    assert pawn.is_move_legal(board, 4, 3)


def test_pawn_cannot_move_two_steps_after_start() -> None:
    """Test pawn cannot move two squares off the starting row."""
    board = Board()
    board.clear()
    pawn = Piece("\u2659", 5, 3, False)
    board.set_piece(5, 3, pawn)
    assert not pawn.is_move_legal(board, 3, 3)


def test_pawn_cannot_move_forward_into_occupied_square() -> None:
    """Test pawn cannot move straight forward into an occupied square."""
    board = Board()
    board.clear()
    pawn = Piece("\u2659", 6, 3, False)
    blocker = Piece("\u265f", 5, 3, True)
    board.set_piece(6, 3, pawn)
    board.set_piece(5, 3, blocker)
    assert not pawn.is_move_legal(board, 5, 3)


def test_pawn_can_capture_enemy_diagonally() -> None:
    """Test pawn can capture enemy one step diagonally forward."""
    board = Board()
    board.clear()
    pawn = Piece("\u2659", 6, 3, False)
    enemy = Piece("\u265f", 5, 4, True)
    board.set_piece(6, 3, pawn)
    board.set_piece(5, 4, enemy)
    assert pawn.is_move_legal(board, 5, 4)


def test_pawn_cannot_capture_ally_diagonally() -> None:
    """Test pawn cannot capture ally one step diagonally forward."""
    board = Board()
    board.clear()
    pawn = Piece("\u2659", 6, 3, False)
    ally = Piece("\u2659", 5, 4, False)
    board.set_piece(6, 3, pawn)
    board.set_piece(5, 4, ally)
    assert not pawn.is_move_legal(board, 5, 4)


def test_pawn_cannot_move_diagonally_without_capture() -> None:
    """Test pawn cannot move diagonally when destination is empty."""
    board = Board()
    board.clear()
    pawn = Piece("\u2659", 6, 3, False)
    board.set_piece(6, 3, pawn)
    assert not pawn.is_move_legal(board, 5, 4)


def test_black_pawn_direction_and_capture() -> None:
    """Test black pawn moves downward and captures diagonally."""
    board = Board()
    board.clear()
    pawn = Piece("\u265f", 1, 3, True)
    enemy = Piece("\u2659", 2, 4, False)
    board.set_piece(1, 3, pawn)
    board.set_piece(2, 4, enemy)
    assert pawn.is_move_legal(board, 2, 3)
    assert pawn.is_move_legal(board, 3, 3)
    assert pawn.is_move_legal(board, 2, 4)
