# CLI-Chess

A simple 2-player, command-line chess game implemented by Python.

## User Guidance

### Requirements

- Vanilla [Python 3 Environment](https://www.python.org/downloads/). No third-party library is needed to run the game.
- A terminal that supports **Unicode** chess symbols (most terminal apps in Windows, MacOS, and Linux do). If pieces look like boxes, switch to a font with better Unicode support. This game is developed and visually verified in **light mode**. However, if the users use the **dark mode**, the perceived black/white piece colors may look reversed between players.

### How to Start

To run the game on a local machine, first clone the repository from GitHub and create a virtual environment:

```bash
git clone https://github.com/Williamzcy0929/CLI-Chess.git
cd CLI-Chess
python3 -m venv .venv
source .venv/bin/activate
```

Then, run the CLI entry from the repository root:

```bash
python chess.py
```

### How to Play

- **Two players** take turns on the **same** computer and the **same** terminal window. No online PVP or AI opponent features are supported.
- **White moves first**, then Black, alternating each successful move.
- After each successful move, the board is printed with **row indices 0–7** on the left and **column indices 0–7** along the top. At the standard start, **row 0** is Black’s back rank and **row 7** is White’s back rank; **column 0** is the **a-file** and **column 7** is the **h-file**.

### Entering a Move

When asked for a move, type **four integers separated by commas**, with **no spaces**. The input format should be:

`start_row,start_col,end_row,end_col`

Examples (standard starting position):

- White king’s pawn one square: `6,4,5,4`
- Black king’s pawn one square: `1,4,2,4`

If the format is wrong, the square is empty, it is not your piece, or the move is illegal, you will see **Invalid Input or Illegal movement!** (or a short turn reminder) and the same side moves again.

### Pawn Promotion

When a pawn reaches the **far rank** (White to **row 0**, Black to **row 7**), the game asks which piece to promote to. Enter one of: **Rook**, **Bishop**, **Knight**, **Queen** (exact spelling, case-sensitive), then confirm with **Y** when prompted.

### How the Game Ends

The game ends when a **king is captured** (the side that lost its king loses). Unfortunately, this game does **not** implement checkmate, stalemate, castling, or any other complex rules in the real chess game.

## Developer Guidance

### Repository Layout

| Path | Role |
| ------ | ------ |
| `chess.py` | CLI entry: adds `src/` to `sys.path` and calls `run_game()` from `game`. |
| `src/game.py` | Interactive loop: user inputs, parses moves, turn order, pawn promotion hooks. |
| `src/board.py` | 8×8 grid, move application, path checks, win detection (kings present). |
| `src/fen.py` | `Fen` helper to load a **board placement** string (FEN piece field) onto a `Board`. |
| `src/piece.py` | `Piece` type: Unicode characters, dispatches legality to `pieces/*`, promotion UI. |
| `src/pieces/` | Per-piece legality: `pawn`, `rook`, `knight`, `bishop`, `queen`, `king`. |
| `tests/` | Pytest suite mirroring the above (`test_board`, `test_fen`, `test_game`, `tests/pieces/test_*.py`). |

### Running Tests

Install pytest (for example `python3 -m pip install pytest`), then from the repo root:

```bash
python3 -m pytest
```

Run a test for a specific module. For example, to run the test for the game interface, please run:

```bash
python3 -m pytest tests/test_game.py
```

#### Test Cases

- `tests/test_game.py` (CLI game loop via mocked input/output, **no CLI interaction is needed**):
  - A marginal case where the player input is non-numeric text, and the game should reject it without crashing.
  - A marginal case where the source and destination squares are the same, and the move should be rejected.
  - A marginal case where one coordinate is out of bounds, and the move should be rejected.
  - A marginal case where the player attempts to capture their own piece, and the move should be rejected.

- `tests/test_board.py` (board-level helper functions):
  - A normal case where the source and destination are valid for a black piece on black's turn.
  - A normal case where the source and destination are valid for a white piece on white's turn.
  - A normal case where the destination has an opponent piece, and capture is allowed by color validation.
  - A normal case where horizontal path checking returns true for a clear path.
  - A normal case where vertical path checking returns true for a clear path.
  - A normal case where diagonal path checking returns true for a clear path.
  - A normal case where adjacent-square checking returns true for horizontal, vertical, diagonal neighbors, and the same square.
  - An error case where the source piece color does not match the active player's turn.
  - An error case where source coordinates are out of bounds.
  - An error case where destination coordinates are out of bounds.
  - An error case where the source square is empty.
  - An error case where the destination is occupied by a same-color piece.
  - An error case where horizontal path checking fails due to a blocker.
  - An error case where vertical path checking fails due to a blocker.
  - An error case where diagonal path checking fails due to a blocker.
  - An error case where horizontal/vertical/diagonal validation is called with incompatible geometry and should return false.
  - An error case where adjacent-square checking is used on a non-neighbor square and should return false.

- `tests/test_fen.py` (FEN loading, move application, basic chess rules, and game-over checks):
  - A normal case where FEN loading places expected pieces on exact board squares.
  - A normal case where FEN character mapping to Unicode chess symbols is correct (white king and black king).
  - A normal case where FEN digits correctly map to consecutive empty squares.
  - A normal case where a legal move returns true.
  - A normal case where a successful move clears the source square and sets the destination square.
  - A normal case where a moved piece keeps its character and updates internal row/column fields.
  - A normal case where the game is not over when both kings are present.
  - A marginal case where loading a new FEN should clear the previously loaded board state.
  - An error case where the move source square is empty, and the move execution should return false.
  - An error case where a piece is asked to move illegally, and the move execution should return false.
  - An error case where a failed move must keep the board unchanged at the source and destination.
  - A marginal case where the game is over because one king is missing (both missing-white and missing-black variants are tested).

- `tests/pieces/test_pawn.py` (pawn movement rules):
  - A normal case where a white pawn moves one step forward into an empty square.
  - A normal case where a white pawn moves two steps from its starting row.
  - A normal case where a white pawn captures an enemy piece diagonally.
  - A normal case where a black pawn moves in the correct forward direction and captures diagonally.
  - An error case where a pawn attempts a two-step move from a non-starting row.
  - An error case where a pawn attempts to move forward into an occupied square.
  - An error case where a pawn attempts to capture a same-color piece diagonally.
  - An error case where a pawn attempts diagonal movement without a capture target.

- `tests/pieces/test_rook.py` (rook movement rules):
  - A normal case where a rook moves horizontally and vertically along clear paths.
  - A normal case where a rook captures an enemy piece on a clear straight path.
  - An error case where a rook attempts non-straight movement.
  - An error case where a rook attempts to capture a piece of the same color.
  - An error case where a rook path is blocked by an intervening piece.

- `tests/pieces/test_knight.py` (knight movement rules):
  - A normal case where a knight performs legal L-shape movement.
  - A normal case where a knight captures an enemy on a legal destination square.
  - A normal case where a knight can jump over an intervening piece.
  - An error case where a knight attempts non-L-shape movement.
  - An error case where a knight attempts to capture a piece of the same color.

- `tests/pieces/test_bishop.py` (bishop movement rules):
  - A normal case where a bishop moves diagonally on a clear path.
  - A normal case where a bishop captures an enemy on a diagonal square.
  - An error case where a bishop attempts non-diagonal movement.
  - An error case where a bishop attempts to capture a same-color piece.
  - An error case where a bishop's diagonal path is blocked.

- `tests/pieces/test_queen.py` (queen movement rules):
  - A normal case where a queen moves horizontally, vertically, and diagonally on clear paths.
  - A normal case where a queen captures an enemy on a legal, clear path.
  - An error case where a queen attempts movement that is neither straight nor diagonal.
  - An error case where a queen attempts to capture a piece of the same color.
  - An error case where a queen path is blocked by an intervening piece.

- `tests/pieces/test_king.py` (king movement rules):
  - A normal case where a king moves one square in horizontal, vertical, and diagonal directions.
  - A normal case where a king captures an adjacent enemy piece.
  - An error case where a king attempts to move more than one square.
  - An error case where a king attempts to capture a piece of the same color.
  - A marginal case where a distant destination remains illegal even when an unrelated blocker exists on board.

## Gen-AI Usage

We used `Cursor Compressor 2`, `Claude Sonnet 4.6`, and `ChatGPT 5.4 Thinking` for brainstorming, searching, and formatting in this repo. We used `ChatGPT 5.4 Thinking` to learn the Forsyth–Edwards Notation (FEN) and implemented it as the primary UI of the game, as well as the Unicode representation for each piece. We used `Claude Sonnet 4.6` to brainstorm the marginal cases for all tests. We used `Cursor Compressor 2` to debug and fix bugs, especially those affecting piece movement, to generate comments and format the code to pass the `Ruff` check, to ensure the coherence of logic across different parts contributed by different group members, and to generate some code that was beyond our scope, such as the CLI UI in `chess.py`.

The class `Fen` was generated by `Cursor Compressor 2` under the supervision of group members. Most of the marginal-case tests were brainstormed by `Claude Sonnet 4.6`, screened by group members, and generated code by `Cursor Compressor 2`. Most of the descriptive comments under each function, except the comments in all piece files (e.g., `bishop.py`) and their corresponding tests (e.g., `test_bishop.py`), were generated by `Cursor Compressor 2` with minor modifications by group members. The script of the CLI entry, named `chess.py`, was fully generated by `Cursor Compressor 2`.

We found a bug in the `game.py` module while running `test_game.py`, where the game loop did not
terminate correctly when the mocked test input iterator was exhausted. We used
`Claude Sonnet 4.6` to debug this issue and adopted the fix by handling
`StopIteration` separately and breaking the loop correctly.

## Contributor

- Zhuozhe Wu: Implemented the board and the Forsyth–Edwards Notation (FEN) and their corresponding tests.
- William Zhao: Implemented the logic for all chess pieces and their corresponding tests.
- Jixiao Liu: Implemented the logic of the game and its corresponding test, as well as the command-line UI.
