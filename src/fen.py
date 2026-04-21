"""FEN loader for Board instances."""

from piece import Piece


class Fen:
    """Populate a board using a FEN board-state fragment."""

    @staticmethod
    def load(fen: str, board) -> None:
        """Load the FEN string into the board."""
        rank = 0
        square = 0
        mapping = {
            "p": "\u265f",
            "P": "\u2659",
            "r": "\u265c",
            "R": "\u2656",
            "n": "\u265e",
            "N": "\u2658",
            "b": "\u265d",
            "B": "\u2657",
            "q": "\u265b",
            "Q": "\u2655",
            "k": "\u265a",
            "K": "\u2654",
        }
        board.clear()
        for query in fen:
            if query == "/":
                rank += 1
                square = 0
            elif query.isdigit():
                square += int(query)
            else:
                board.set_piece(
                    rank,
                    square,
                    Piece(mapping[query], rank, square, not query.isupper()),
                )
                square += 1
