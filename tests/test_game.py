"""Tests for CLI game loop behavior."""

from game import run_game

def test_run_game_invalid_input_format() -> None:
    """Non-numeric input should not crash and should prompt the user."""
    outputs: list[str] = []
    inputs = iter(["abc", "7,4,6,4"])
    run_game(
        input_fn=lambda: next(inputs),
        print_fn=lambda msg: outputs.append(str(msg)),
        starting_fen="4k3/8/8/8/8/8/8/4K3",
        max_turns=1,
    )
    assert any("Invalid" in line for line in outputs)


def test_run_game_move_to_same_square() -> None:
    """Moving a piece to its own square should be rejected."""
    outputs: list[str] = []
    inputs = iter(["7,4,7,4"])
    run_game(
        input_fn=lambda: next(inputs),
        print_fn=lambda msg: outputs.append(str(msg)),
        starting_fen="4k3/8/8/8/8/8/8/4K3",
        max_turns=1,
    )
    assert any("Invalid" in line for line in outputs)


def test_run_game_move_out_of_bounds() -> None:
    """Coordinates outside the board should be rejected."""
    outputs: list[str] = []
    inputs = iter(["7,4,8,4"])
    run_game(
        input_fn=lambda: next(inputs),
        print_fn=lambda msg: outputs.append(str(msg)),
        starting_fen="4k3/8/8/8/8/8/8/4K3",
        max_turns=1,
    )
    assert any("Invalid" in line for line in outputs)


def test_run_game_capture_own_piece() -> None:
    """A piece should not be allowed to capture a friendly piece."""
    outputs: list[str] = []
    inputs = iter(["7,4,7,3"])
    run_game(
        input_fn=lambda: next(inputs),
        print_fn=lambda msg: outputs.append(str(msg)),
        starting_fen="4k3/8/8/8/8/8/8/3KK3",
        max_turns=1,
    )
    assert any("Invalid" in line for line in outputs)