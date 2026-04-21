"""Tests for FEN loading and board state transitions."""

from board import Board
from fen import Fen


def test_fen_load_places_expected_pieces() -> None:
    """Load FEN and confirm black king square is populated."""
    board = Board()
    Fen.load("8/8/8/3k4/8/4K3/8/8", board)
    assert board.get_piece(3, 3) is not None


def test_fen_load_places_white_king() -> None:
    """Load FEN and confirm white king square is populated."""
    board = Board()
    Fen.load("8/8/8/3k4/8/4K3/8/8", board)
    assert board.get_piece(5, 4) is not None


def test_fen_load_black_king_character() -> None:
    """Load FEN and verify black king character mapping."""
    board = Board()
    Fen.load("8/8/8/3k4/8/4K3/8/8", board)
    assert board.get_piece(3, 3).get_character() == "\u265a"


def test_fen_load_white_king_character() -> None:
    """Load FEN and verify white king character mapping."""
    board = Board()
    Fen.load("8/8/8/3k4/8/4K3/8/8", board)
    assert board.get_piece(5, 4).get_character() == "\u2654"


def test_fen_load_clears_previous_board_state() -> None:
    """Loading a new FEN should clear previous board pieces."""
    board = Board()
    Fen.load("8/8/8/3k4/8/4K3/8/8", board)
    Fen.load("8/8/8/8/8/8/8/8", board)
    assert board.get_piece(3, 3) is None
    assert board.get_piece(5, 4) is None


def test_fen_load_digit_leaves_empty_squares() -> None:
    """Digit segments in FEN should map to empty squares."""
    board = Board()
    Fen.load("8/8/8/3k4/8/4K3/8/8", board)
    assert board.get_piece(3, 0) is None
    assert board.get_piece(3, 1) is None
    assert board.get_piece(3, 2) is None


def test_move_piece_returns_true_for_legal_move() -> None:
    """Legal board move should return true."""
    board = Board()
    Fen.load("8/8/8/8/8/8/4P3/8", board)
    assert board.move_piece(6, 4, 4, 4)


def test_move_piece_clears_source_square() -> None:
    """Successful move should clear source square."""
    board = Board()
    Fen.load("8/8/8/8/8/8/4P3/8", board)
    board.move_piece(6, 4, 4, 4)
    assert board.get_piece(6, 4) is None


def test_move_piece_sets_destination_square() -> None:
    """Successful move should populate destination square."""
    board = Board()
    Fen.load("8/8/8/8/8/8/4P3/8", board)
    board.move_piece(6, 4, 4, 4)
    assert board.get_piece(4, 4) is not None


def test_move_piece_preserves_piece_character() -> None:
    """Moved piece should preserve its unicode character."""
    board = Board()
    Fen.load("8/8/8/8/8/8/4P3/8", board)
    board.move_piece(6, 4, 4, 4)
    assert board.get_piece(4, 4).get_character() == "\u2659"


def test_move_piece_returns_false_for_empty_source() -> None:
    """Move should fail when source square is empty."""
    board = Board()
    Fen.load("8/8/8/8/8/8/4P3/8", board)
    assert not board.move_piece(5, 5, 4, 5)


def test_move_piece_returns_false_for_illegal_move() -> None:
    """Move should fail for illegal piece movement."""
    board = Board()
    Fen.load("8/8/8/8/8/8/4P3/8", board)
    assert not board.move_piece(6, 4, 3, 4)


def test_move_piece_failed_move_keeps_board_unchanged() -> None:
    """Failed move should not mutate source or destination squares."""
    board = Board()
    Fen.load("8/8/8/8/8/8/4P3/8", board)
    board.move_piece(6, 4, 3, 4)
    assert board.get_piece(6, 4) is not None
    assert board.get_piece(3, 4) is None


def test_move_piece_updates_piece_position() -> None:
    """Successful move should update piece row and col fields."""
    board = Board()
    Fen.load("8/8/8/8/8/8/4P3/8", board)
    board.move_piece(6, 4, 4, 4)
    piece = board.get_piece(4, 4)
    assert piece.row == 4
    assert piece.col == 4


def test_game_over_when_one_king_missing() -> None:
    """Game should end when one king is absent."""
    board = Board()
    Fen.load("8/8/8/8/8/8/8/4K3", board)
    assert board.is_game_over(print_fn=lambda _: None)


def test_game_not_over_when_both_kings_exist() -> None:
    """Game should continue when both kings are present."""
    board = Board()
    Fen.load("4k3/8/8/8/8/8/8/4K3", board)
    assert not board.is_game_over(print_fn=lambda _: None)


def test_game_over_when_white_king_missing() -> None:
    """Game should end when white king is missing."""
    board = Board()
    Fen.load("4k3/8/8/8/8/8/8/8", board)
    assert board.is_game_over(print_fn=lambda _: None)