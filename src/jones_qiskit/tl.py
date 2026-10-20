"""Temperley–Lieb algebra TL_n(δ).  Session 1 — HUMAN-AUTHORED (see CLAUDE.md).

Suggested representation: a TL diagram on n strands as a perfect matching of the
2n boundary points (0..n-1 on the bottom, n..2n-1 on top), stored as a tuple
`pairs` with pairs[a] = b iff a and b are joined. You may change the internals
freely; the tests only use the functions below.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class TLDiagram:
    n: int
    pairs: tuple[int, ...]


def delta(k: int) -> float:
    """Loop value δ = 2cos(π/k)."""
    raise NotImplementedError("Session 1")


def identity(n: int) -> TLDiagram:
    raise NotImplementedError("Session 1")


def e(i: int, n: int) -> TLDiagram:
    """Generator e_i (1 <= i <= n-1): cup-cap on strands i, i+1."""
    raise NotImplementedError("Session 1")


def compose(a: TLDiagram, b: TLDiagram) -> tuple[int, TLDiagram]:
    """Stack a on top of b. Return (number of closed loops removed, resulting diagram)."""
    raise NotImplementedError("Session 1")
