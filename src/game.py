"""CLI game interface."""

from __future__ import annotations

from board import Board
from fen import Fen

STARTING_FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"


def run_game(
    input_fn=input,
    print_fn=print,
    starting_fen: str = STARTING_FEN,
    max_turns: int | None = None,
) -> None:
    """Run an interactive two-player CLI chess game."""
    board = Board()
    Fen.load(starting_fen, board)
    black_turn = False
    turns_played = 0

    while not board.is_game_over(print_fn=print_fn):
        if max_turns is not None and turns_played >= max_turns:
            break
        try:
            print_fn(board)
            if not black_turn:
                print_fn(
                    "White's turn. What is your move? "
                    "Format:[start row],[start col],[end row],[end col] "
                    "example: 6,6,5,6"
                )
            else:
                print_fn(
                    "Black's turn. What is your move? "
                    "Format:[start row],[start col],[end row],[end col] "
                    "example: 1,6,2,6"
                )

            op = input_fn().strip()
            parts = [int(value.strip()) for value in op.split(",")]
            if len(parts) != 4:
                raise ValueError(
                    "Move must contain four comma-separated integers.",
                )
            start_row, start_col, end_row, end_col = parts

            current_piece = board.get_piece(start_row, start_col)
            if (
                current_piece is None
                or current_piece.get_is_black() != black_turn
            ):
                if black_turn:
                    print_fn("It is black's turn now.")
                    print_fn("Select a black piece and move.")
                else:
                    print_fn("It is white's turn now.")
                    print_fn("Select a white piece and move.")
                continue

            if not board.move_piece(start_row, start_col, end_row, end_col):
                print_fn("Invalid Input or Illegal movement!")
                continue

            moved_piece = board.get_piece(end_row, end_col)
            if moved_piece is not None:
                if moved_piece.get_character() == "\u2659" and end_row == 0:
                    moved_piece.promote_pawn(
                        0,
                        False,
                        input_fn=input_fn,
                        print_fn=print_fn,
                    )
                if moved_piece.get_character() == "\u265f" and end_row == 7:
                    moved_piece.promote_pawn(
                        7,
                        True,
                        input_fn=input_fn,
                        print_fn=print_fn,
                    )

            if board.is_game_over(print_fn=print_fn):
                break
            black_turn = not black_turn
            turns_played += 1
        except Exception:
            print_fn("Invalid Input or Illegal movement!")


if __name__ == "__main__":
    run_game()
