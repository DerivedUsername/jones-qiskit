"""Path basis → qubits; braid words → Qiskit gates.  Session 5 — HUMAN-AUTHORED."""

from __future__ import annotations

from qiskit.circuit import Gate


def n_qubits(n: int, k: int) -> int:
    raise NotImplementedError("Session 5")


def braid_gate(word: list[int], n: int, k: int) -> Gate:
    """Gate implementing the braid's path-model unitary (UnitaryGate is fine to start)."""
    raise NotImplementedError("Session 5")
