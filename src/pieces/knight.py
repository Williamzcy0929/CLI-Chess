"""Class Knight."""

from board import Board

class Knight:
    """Class Knight."""
    def __init__(self, row: int, col: int, is_black: bool) -> None:
        """Initialize the Knight."""
        self.row = row
        self.col = col
        self.is_black = is_black

    def verify_knight(self, end_row: int, end_col: int) -> bool:
        """Verify the knight move."""
        changed_row = abs(end_row - self.row)
        changed_col = abs(end_col - self.col)
        return (
            (changed_col == 2 and changed_row == 1)
            or (changed_col == 1 and changed_row == 2)
        )

    def is_move_legal(self, board, end_row: int, end_col: int) -> bool:
        """Check if the move is legal."""
        if not board.verify_source_and_destination(
            self.row,
            self.col,
            end_row,
            end_col,
            self.is_black,
        ):
            return False
        return self.verify_knight(end_row, end_col)