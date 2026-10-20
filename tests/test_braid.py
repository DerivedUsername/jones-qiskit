"""Session 2: braid group representation on the path basis."""

import numpy as np
import pytest
from _util import call_or_skip

from jones_qiskit import braid

K = 5


@pytest.mark.parametrize("n", [3, 4])
def test_unitary(n):
    for i in range(1, n):
        m = call_or_skip(braid.generator_matrix, i, n, K)
        assert np.allclose(m @ m.conj().T, np.eye(len(m)))


@pytest.mark.parametrize("n", [3, 4])
def test_inverse(n):
    u = call_or_skip(braid.braid_to_unitary, [1, -1], n, K)
    assert np.allclose(u, np.eye(len(u)))


@pytest.mark.parametrize("n", [3, 4])
def test_braid_relation(n):
    for i in range(1, n - 1):
        lhs = call_or_skip(braid.braid_to_unitary, [i, i + 1, i], n, K)
        rhs = call_or_skip(braid.braid_to_unitary, [i + 1, i, i + 1], n, K)
        assert np.allclose(lhs, rhs)


def test_far_commutation():
    a = call_or_skip(braid.braid_to_unitary, [1, 3], 4, K)
    b = call_or_skip(braid.braid_to_unitary, [3, 1], 4, K)
    assert np.allclose(a, b)
