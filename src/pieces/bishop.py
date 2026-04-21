"""Class Bishop."""

from board import Board

class Bishop:
    """Class Bishop."""
    def __init__(self, row: int, col: int, is_black: bool) -> None:
        """Initialize the Bishop."""
        self.row = row
        self.col = col
        self.is_black = is_black

    def is_move_legal(self, board: Board, end_row: int, end_col: int) -> bool:
        """Check if the move is legal."""
        if not board.verify_source_and_destination(
            self.row,
            self.col,
            end_row,
            end_col,
            self.is_black,
        ):
            return False
        return board.verify_diagonal(self.row, self.col, end_row, end_col)