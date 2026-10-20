"""Braid words → unitaries on the path basis.  Session 2 — HUMAN-AUTHORED (see CLAUDE.md).

Path basis: walks of length n on the Dynkin graph A_{k-1} (vertices 1..k-1)
starting at vertex 1. The braid generator σ_i acts locally at step i through the
Jones–Wenzl / TL representation at q = e^{iπ/k}.
"""

from __future__ import annotations

import numpy as np


def path_basis(n: int, k: int) -> list[tuple[int, ...]]:
    raise NotImplementedError("Session 2")


def generator_matrix(i: int, n: int, k: int, inverse: bool = False) -> np.ndarray:
    """Matrix of σ_i (or σ_i^{-1}) on the path basis."""
    raise NotImplementedError("Session 2")


def braid_to_unitary(word: list[int], n: int, k: int) -> np.ndarray:
    """Product of generator matrices for a braid word (i = σ_i, -i = σ_i^{-1})."""
    raise NotImplementedError("Session 2")
