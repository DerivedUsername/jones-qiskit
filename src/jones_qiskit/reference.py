"""Known Jones polynomials, as {exponent: coefficient} in the variable t.

Mirror images are related by t -> t^{-1}; which chirality the closure of σ₁³
gives depends on the crossing convention fixed in Session 3, so tests accept
either mirror.
"""

from __future__ import annotations

import cmath

UNKNOT = {0: 1}
TREFOIL_RIGHT = {1: 1, 3: 1, 4: -1}  # t + t^3 - t^4
FIGURE_EIGHT = {2: 1, 1: -1, 0: 1, -1: -1, -2: 1}  # amphichiral

# braid word, number of strands, polynomial
KNOTS = {
    "unknot": ([], 1, UNKNOT),
    "trefoil": ([1, 1, 1], 2, TREFOIL_RIGHT),
    "figure-eight": ([1, -2, 1, -2], 3, FIGURE_EIGHT),
}


def mirror(poly: dict[int, int]) -> dict[int, int]:
    return {-e: c for e, c in poly.items()}


def evaluate(poly: dict[int, int], t: complex) -> complex:
    return sum(c * t**e for e, c in poly.items())


def root(k: int) -> complex:
    """AJL evaluation point t = e^{2πi/k}."""
    return cmath.exp(2j * cmath.pi / k)
