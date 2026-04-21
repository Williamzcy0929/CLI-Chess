"""Tests for FEN loading and board state transitions."""

from cli_chess.board import Board
from cli_chess.fen import Fen


def test_fen_load_places_expected_pieces() -> None:
    board = Board()
    Fen.load("8/8/8/3k4/8/4K3/8/8", board)
    assert board.get_piece(3, 3) is not None


def test_fen_load_places_white_king() -> None:
    board = Board()
    Fen.load("8/8/8/3k4/8/4K3/8/8", board)
    assert board.get_piece(5, 4) is not None


def test_fen_load_black_king_character() -> None:
    board = Board()
    Fen.load("8/8/8/3k4/8/4K3/8/8", board)
    assert board.get_piece(3, 3).get_character() == "\u265a"


def test_fen_load_white_king_character() -> None:
    board = Board()
    Fen.load("8/8/8/3k4/8/4K3/8/8", board)
    assert board.get_piece(5, 4).get_character() == "\u2654"


def test_fen_load_clears_previous_board_state() -> None:
    board = Board()
    Fen.load("8/8/8/3k4/8/4K3/8/8", board)
    Fen.load("8/8/8/8/8/8/8/8", board)
    assert board.get_piece(3, 3) is None
    assert board.get_piece(5, 4) is None


def test_fen_load_digit_leaves_empty_squares() -> None:
    board = Board()
    Fen.load("8/8/8/3k4/8/4K3/8/8", board)
    assert board.get_piece(3, 0) is None
    assert board.get_piece(3, 1) is None
    assert board.get_piece(3, 2) is None


def test_move_piece_returns_true_for_legal_move() -> None:
    board = Board()
    Fen.load("8/8/8/8/8/8/4P3/8", board)
    assert board.move_piece(6, 4, 4, 4)


def test_move_piece_clears_source_square() -> None:
    board = Board()
    Fen.load("8/8/8/8/8/8/4P3/8", board)
    board.move_piece(6, 4, 4, 4)
    assert board.get_piece(6, 4) is None


def test_move_piece_sets_destination_square() -> None:
    board = Board()
    Fen.load("8/8/8/8/8/8/4P3/8", board)
    board.move_piece(6, 4, 4, 4)
    assert board.get_piece(4, 4) is not None


def test_move_piece_preserves_piece_character() -> None:
    board = Board()
    Fen.load("8/8/8/8/8/8/4P3/8", board)
    board.move_piece(6, 4, 4, 4)
    assert board.get_piece(4, 4).get_character() == "\u2659"


def test_move_piece_returns_false_for_empty_source() -> None:
    board = Board()
    Fen.load("8/8/8/8/8/8/4P3/8", board)
    assert not board.move_piece(5, 5, 4, 5)


def test_move_piece_returns_false_for_illegal_move() -> None:
    board = Board()
    Fen.load("8/8/8/8/8/8/4P3/8", board)
    assert not board.move_piece(6, 4, 3, 4)


def test_move_piece_failed_move_keeps_board_unchanged() -> None:
    board = Board()
    Fen.load("8/8/8/8/8/8/4P3/8", board)
    board.move_piece(6, 4, 3, 4)
    assert board.get_piece(6, 4) is not None
    assert board.get_piece(3, 4) is None


def test_move_piece_updates_piece_position() -> None:
    board = Board()
    Fen.load("8/8/8/8/8/8/4P3/8", board)
    board.move_piece(6, 4, 4, 4)
    piece = board.get_piece(4, 4)
    assert piece.row == 4
    assert piece.col == 4


def test_game_over_when_one_king_missing() -> None:
    board = Board()
    Fen.load("8/8/8/8/8/8/8/4K3", board)
    assert board.is_game_over(print_fn=lambda _: None)


def test_game_not_over_when_both_kings_exist() -> None:
    board = Board()
    Fen.load("4k3/8/8/8/8/8/8/4K3", board)
    assert not board.is_game_over(print_fn=lambda _: None)


def test_game_over_when_white_king_missing() -> None:
    board = Board()
    Fen.load("4k3/8/8/8/8/8/8/8", board)
    assert board.is_game_over(print_fn=lambda _: None)