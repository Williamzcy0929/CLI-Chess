"""Class Board as the chess board."""

from __future__ import annotations

from piece import Piece


class Board:
    """Chess board."""

    def __init__(self) -> None:
        """Initialize an empty 8x8 board."""
        self.board: list[list[Piece | None]] = [
            [None for _ in range(8)] for _ in range(8)
        ]

    def get_piece(self, row: int, col: int) -> Piece | None:
        """Return the piece at the given square."""
        return self.board[row][col]

    def set_piece(self, row: int, col: int, piece: Piece | None) -> None:
        """Place a piece at the given square."""
        self.board[row][col] = piece

    def move_piece(
        self,
        start_row: int,
        start_col: int,
        end_row: int,
        end_col: int,
    ) -> bool:
        """Move a piece if the requested move is legal."""
        moving_piece = self.board[start_row][start_col]
        if (
            moving_piece is not None
            and moving_piece.is_move_legal(self, end_row, end_col)
        ):
            self.board[end_row][end_col] = moving_piece
            moving_piece.set_position(end_row, end_col)
            self.board[start_row][start_col] = None
            return True
        return False

    def is_game_over(self, print_fn=print) -> bool:
        """Return whether one king has been captured."""
        white_king = False
        black_king = False
        for row in self.board:
            for piece in row:
                if piece is None:
                    continue
                if piece.get_character() == "\u2654":
                    white_king = True
                if piece.get_character() == "\u265a":
                    black_king = True
        if not white_king:
            print_fn("Black win!")
            return True
        if not black_king:
            print_fn("White win!")
            return True
        return False

    def clear(self) -> None:
        """Remove all pieces from the board."""
        for row in range(8):
            for col in range(8):
                self.board[row][col] = None

    def verify_source_and_destination(
        self,
        start_row: int,
        start_col: int,
        end_row: int,
        end_col: int,
        is_black: bool,
    ) -> bool:
        """Validate source and destination squares for a move."""
        in_bounds = (
            0 <= start_row < 8
            and 0 <= start_col < 8
            and 0 <= end_row < 8
            and 0 <= end_col < 8
        )
        if not in_bounds:
            return False
        source = self.board[start_row][start_col]
        if source is None:
            return False
        if source.get_is_black() != is_black:
            return False
        destination = self.board[end_row][end_col]
        return destination is None or destination.get_is_black() != is_black

    def verify_adjacent(
        self,
        start_row: int,
        start_col: int,
        end_row: int,
        end_col: int,
    ) -> bool:
        """Return whether destination is adjacent to source."""
        return (
            (
                start_row == end_row
                or start_row + 1 == end_row
                or start_row - 1 == end_row
            )
            and (
                start_col == end_col
                or start_col + 1 == end_col
                or start_col - 1 == end_col
            )
        )

    def verify_horizontal(
        self,
        start_row: int,
        start_col: int,
        end_row: int,
        end_col: int,
    ) -> bool:
        """Return whether a horizontal path is clear."""
        if start_row != end_row:
            return False
        for col in range(min(start_col, end_col) + 1, max(start_col, end_col)):
            if self.board[start_row][col] is not None:
                return False
        return True

    def verify_vertical(
        self,
        start_row: int,
        start_col: int,
        end_row: int,
        end_col: int,
    ) -> bool:
        """Return whether a vertical path is clear."""
        if start_col != end_col:
            return False
        for row in range(min(start_row, end_row) + 1, max(start_row, end_row)):
            if self.board[row][start_col] is not None:
                return False
        return True

    def verify_diagonal(
        self,
        start_row: int,
        start_col: int,
        end_row: int,
        end_col: int,
    ) -> bool:
        """Return whether a diagonal path is clear."""
        changed_row = abs(start_row - end_row)
        changed_col = abs(start_col - end_col)
        if changed_row != changed_col:
            return False
        row_change = 1 if end_row > start_row else -1
        col_change = 1 if end_col > start_col else -1
        for i in range(1, changed_row):
            new_row = start_row + i * row_change
            new_col = start_col + i * col_change
            if self.board[new_row][new_col] is not None:
                return False
        return True

    def __str__(self) -> str:
        """Return a printable board representation."""
        out = [" " + "".join(f" {i}" for i in range(8))]
        for row in range(8):
            cells = []
            for col in range(8):
                piece = self.board[row][col]
                cells.append(str(piece) if piece is not None else "\u2001")
            out.append(f"{row}|{'|'.join(cells)}|")
        return "\n".join(out) + "\n"