"""Session 3: exact Jones values match the reference polynomials (either mirror)."""

import pytest
from _util import call_or_skip

from jones_qiskit.jones_exact import jones_at_root
from jones_qiskit.reference import KNOTS, evaluate, mirror, root

K = 5


@pytest.mark.parametrize("name", KNOTS)
def test_matches_reference(name):
    word, n, poly = KNOTS[name]
    got = call_or_skip(jones_at_root, word, n, K)
    t = root(K)
    candidates = [evaluate(poly, t), evaluate(mirror(poly), t)]
    assert any(abs(got - c) < 1e-9 for c in candidates), (got, candidates)
