"""Session 1: Temperley–Lieb relations."""

import math

import pytest
from _util import call_or_skip

from jones_qiskit import tl


def test_delta():
    assert call_or_skip(tl.delta, 5) == pytest.approx(2 * math.cos(math.pi / 5))


@pytest.mark.parametrize("n", [3, 4, 5])
def test_idempotent_up_to_loop(n):
    for i in range(1, n):
        ei = call_or_skip(tl.e, i, n)
        loops, d = call_or_skip(tl.compose, ei, ei)
        assert loops == 1 and d == ei  # e_i^2 = δ e_i


@pytest.mark.parametrize("n", [3, 4, 5])
def test_jones_relation(n):
    for i in range(1, n - 1):
        a, b = call_or_skip(tl.e, i, n), call_or_skip(tl.e, i + 1, n)
        l1, ab = call_or_skip(tl.compose, a, b)
        l2, aba = call_or_skip(tl.compose, ab, a)
        assert l1 + l2 == 0 and aba == a  # e_i e_{i+1} e_i = e_i


@pytest.mark.parametrize("n", [4, 5])
def test_far_commutation(n):
    for i in range(1, n):
        for j in range(i + 2, n):
            a, b = call_or_skip(tl.e, i, n), call_or_skip(tl.e, j, n)
            assert call_or_skip(tl.compose, a, b) == call_or_skip(tl.compose, b, a)


def test_identity_is_unit():
    one, e1 = call_or_skip(tl.identity, 3), call_or_skip(tl.e, 1, 3)
    assert call_or_skip(tl.compose, one, e1) == (0, e1)
