"""Hadamard test circuits.  Session 4 — HUMAN-AUTHORED (see CLAUDE.md)."""

from __future__ import annotations

from qiskit import QuantumCircuit
from qiskit.circuit import Gate


def hadamard_test_circuit(u: Gate, imag: bool = False) -> QuantumCircuit:
    """Ancilla-controlled U; measuring the ancilla estimates Re<ψ|U|ψ> (Im if imag)."""
    raise NotImplementedError("Session 4")


def estimate(circuit: QuantumCircuit, shots: int = 4000) -> float:
    """Run on AerSimulator and return P(0) - P(1) for the ancilla."""
    raise NotImplementedError("Session 4")
