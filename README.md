# Jones polynomial estimation in Qiskit

An implementation of the Aharonov–Jones–Landau (AJL) algorithm: a quantum
algorithm that approximates the Jones polynomial of a knot or link at a root of
unity, using a unitary representation of the braid group built from the
Temperley–Lieb algebra. Validated against exact classical values, run under
realistic noise, and on IBM quantum hardware.

> **Status: in progress.** See [docs/sessions.md](docs/sessions.md) for the roadmap.

| Milestone | Status |
|---|---|
| Classical Temperley–Lieb layer | ✅ |
| Braid → unitary (path model) | ⬜ |
| Exact Jones values (ground truth) | ⬜ |
| Hadamard test circuit | ⬜ |
| Full simulator pipeline | ⬜ |
| Noise + error mitigation | ⬜ |
| IBM hardware run | ⬜ |

## Quick start (Windows PowerShell)

```powershell
.\setup.ps1
```

This creates `.venv`, installs dependencies, runs a Bell-state sanity check and
the test suite. On macOS/Linux:

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt && pip install -e .
python hello.py && pytest
```

## Layout

```
src/jones_qiskit/
  tl.py             Temperley–Lieb algebra TL_n(δ)
  braid.py          braid words → unitaries on the path basis
  jones_exact.py    exact Jones values via the Markov trace
  hadamard_test.py  Hadamard test circuits
  encoding.py       path basis → qubits, braid gates
  pipeline.py       braid word in → Jones estimate out
  reference.py      known Jones polynomials for testing
tests/              pytest suite (unimplemented stages skip, not fail)
docs/sessions.md    session-by-session roadmap
```

## Background

*(To be written: the Jones polynomial in three paragraphs, what AJL does, why
the Temperley–Lieb representation makes it work.)*

## Results

*(To be filled from committed notebooks: convergence plot, noisy vs. mitigated,
hardware datapoint.)*

## How this was built

The mathematical core and the quantum circuits were written by hand; AI agents
were used for scaffolding (test harness, CI, plotting, documentation drafts) and
for code review. The split is recorded in [CLAUDE.md](CLAUDE.md).
