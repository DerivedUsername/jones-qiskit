"""Sanity checks on the reference data itself (these run from day one)."""

import cmath

import pytest

from jones_qiskit.reference import KNOTS, evaluate, mirror


@pytest.mark.parametrize("name", KNOTS)
def test_value_at_one(name):
    # V_K(1) = 1 for every knot
    _, _, poly = KNOTS[name]
    assert evaluate(poly, 1) == pytest.approx(1)


@pytest.mark.parametrize("name", KNOTS)
def test_value_at_cube_root_of_unity(name):
    # V_K(e^{2πi/3}) = 1 for every knot
    _, _, poly = KNOTS[name]
    w = cmath.exp(2j * cmath.pi / 3)
    assert evaluate(poly, w) == pytest.approx(1)


def test_figure_eight_amphichiral():
    _, _, poly = KNOTS["figure-eight"]
    assert mirror(poly) == poly
