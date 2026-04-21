"""Shared piece object and behavior dispatch."""

from __future__ import annotations

from .pieces.bishop import Bishop
from .pieces.king import King
from .pieces.knight import Knight
from .pieces.pawn import Pawn
from .pieces.queen import Queen
from .pieces.rook import Rook


class Piece:
    """Represent one chess piece on the board."""

    def __init__(self, character: str, row: int, col: int, is_black: bool) -> None:
        self.character = character
        self.row = row
        self.col = col
        self.is_black = is_black

    def is_move_legal(self, board, end_row: int, end_col: int) -> bool:
        if self.character in ("\u2659", "\u265f"):
            pawn = Pawn(self.row, self.col, self.is_black)
            return pawn.is_move_legal(board, end_row, end_col)
        if self.character in ("\u2656", "\u265c"):
            rook = Rook(self.row, self.col, self.is_black)
            return rook.is_move_legal(board, end_row, end_col)
        if self.character in ("\u2658", "\u265e"):
            knight = Knight(self.row, self.col, self.is_black)
            return knight.is_move_legal(board, end_row, end_col)
        if self.character in ("\u2657", "\u265d"):
            bishop = Bishop(self.row, self.col, self.is_black)
            return bishop.is_move_legal(board, end_row, end_col)
        if self.character in ("\u2655", "\u265b"):
            queen = Queen(self.row, self.col, self.is_black)
            return queen.is_move_legal(board, end_row, end_col)
        if self.character in ("\u2654", "\u265a"):
            king = King(self.row, self.col, self.is_black)
            return king.is_move_legal(board, end_row, end_col)
        return False

    def set_position(self, row: int, col: int) -> None:
        self.row = row
        self.col = col

    def get_is_black(self) -> bool:
        return self.is_black

    def get_character(self) -> str:
        return self.character

    def promote_pawn(self, row: int, is_black: bool, input_fn=input, print_fn=print) -> None:
        new_piece = "\0"
        choice_map = {
            "Rook": ("\u265c", "\u2656"),
            "Bishop": ("\u265d", "\u2657"),
            "Knight": ("\u265e", "\u2658"),
            "Queen": ("\u265b", "\u2655"),
        }
        while True:
            if (is_black and row == 7) or ((not is_black) and row == 0):
                print_fn("Pawn is promoted!")
                print_fn("Enter a piece you want it to be (Rook, Bishop, Knight, Queen):")
            else:
                return
            choice = input_fn().strip()
            if choice not in choice_map:
                print_fn("Enter a piece you want it to be (Rook, Bishop, Knight, Queen):")
                print_fn("Y: Confirm, N: Choose again.")
                continue
            print_fn(f"Your choice is {choice} (Y/N):")
            confirm = input_fn().strip()
            if confirm == "Y":
                black_char, white_char = choice_map[choice]
                new_piece = black_char if is_black else white_char
                break
        self.character = new_piece

    def __str__(self) -> str:
        return self.character
