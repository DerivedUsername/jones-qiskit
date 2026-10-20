"""Exact Jones values via the Markov trace.  Session 3 — DELEGABLE (see CLAUDE.md)."""

from __future__ import annotations


def jones_at_root(word: list[int], n: int, k: int) -> complex:
    """V_L(t) at t = e^{2πi/k} for the trace closure of `word` on n strands.

    Must include the writhe and loop-value normalization, so that the result is
    the honest Jones polynomial value (unknot -> 1).
    """
    raise NotImplementedError("Session 3")
