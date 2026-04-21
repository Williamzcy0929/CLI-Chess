"""Root entry point for the CLI chess game."""

from __future__ import annotations

import sys
from pathlib import Path


def run_game() -> None:
    """Run the CLI chess game."""
    repo_root = Path(__file__).resolve().parent
    src_dir = repo_root / "src"
    if str(src_dir) not in sys.path:
        sys.path.insert(0, str(src_dir))

    from game import run_game

    run_game()

if __name__ == "__main__":
    run_game()