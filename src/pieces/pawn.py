"""Class Pawn."""

from board import Board

class Pawn:
    """Class Pawn."""
    def __init__(self, row: int, col: int, is_black: bool) -> None:
        """Initialize the Pawn."""
        self.row = row
        self.col = col
        self.is_black = is_black

    def is_move_legal(self, board, end_row: int, end_col: int) -> bool:
        """Check if the move is legal."""
        if (
            board.verify_vertical(self.row, self.col, end_row, end_col)
            and board.get_piece(end_row, end_col) is None
        ):
            if self.is_black:
                return end_row == self.row + 1 or (
                    end_row == self.row + 2 and self.row == 1
                )
            return end_row == self.row - 1 or (
                end_row == self.row - 2 and self.row == 6
            )
        if self.col == end_col + 1 or self.col == end_col - 1:
            target = board.get_piece(end_row, end_col)
            if target is not None and target.get_is_black() != self.is_black:
                if self.is_black:
                    return end_row == self.row + 1
                return end_row == self.row - 1
            return False
        return False
