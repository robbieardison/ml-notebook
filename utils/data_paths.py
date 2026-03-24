"""Resolve `data/` directory for notebooks run from repo root or any `course/` subfolder."""

from __future__ import annotations

from pathlib import Path


def repo_root() -> Path:
    """Walk upward from cwd until we find the ml-notebook root (has `data/` and `course/`)."""
    p = Path.cwd().resolve()
    for _ in range(12):
        if (p / "data").is_dir() and (p / "course").is_dir():
            return p
        if p.parent == p:
            break
        p = p.parent
    raise FileNotFoundError(
        "Could not locate repository root (expected a folder containing both 'data/' and 'course/'). "
        "Start Jupyter from the ml-notebook directory or open a notebook under course/."
    )


def data_dir() -> Path:
    return repo_root() / "data"
