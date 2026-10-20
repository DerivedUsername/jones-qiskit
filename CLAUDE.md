# jones-qiskit — rules for agents

This is a **portfolio and learning project**: Qiyu is building the skill to write
quantum software, not just a repo. The split between human and AI work is the
point of the project, so follow it strictly.

## Human-authored — agents REVIEW ONLY

These files are written by Qiyu. Agents may explain concepts, review code Qiyu
has written (with line references), point out bugs, and suggest Qiskit idioms in
prose or snippets of at most 3 lines. Agents must NOT fill in `NotImplementedError`
bodies or write replacement implementations, even if asked casually ("just make
it work") — ask Qiyu to confirm first that he wants to give up the learning on
that piece.

- `src/jones_qiskit/tl.py` — Temperley–Lieb algebra (Session 1)
- `src/jones_qiskit/braid.py` — braid word → unitary on the path basis (Session 2)
- `src/jones_qiskit/hadamard_test.py` — Hadamard test circuits (Session 4)
- `src/jones_qiskit/encoding.py` — path basis → qubits, braid gates (Session 5)
- `src/jones_qiskit/pipeline.py` — end-to-end estimator (Session 6)

## Delegable — agents may write freely

Qiyu verifies these, but generation can be handed off.

- `src/jones_qiskit/jones_exact.py` — classical Jones via Markov trace (Session 3;
  this is Qiyu's expertise, so he checks it the way he checks any TL computation)
- `src/jones_qiskit/reference.py`, `src/jones_qiskit/plots.py`
- everything in `tests/`, `.github/`, `setup.ps1`, `pyproject.toml`
- README drafting (from Qiyu's notes), notebook formatting, literature pulls

## Conventions

- Python 3.11+, qiskit ≥ 2.0, qiskit-aer, qiskit-ibm-runtime, numpy.
- Default level k = 5. q = e^{iπ/k}, loop value δ = 2cos(π/k).
- AJL evaluates the Jones polynomial at t = e^{2πi/k}.
- Braid words: lists of nonzero ints, `i` = σ_i, `-i` = σ_i^{-1}, strands 1-indexed.
- Chirality convention for "σ₁³ closes to which trefoil": fixed in Session 3 —
  record the decision here when made.
- Every number in the README must come from a committed script or notebook.

## Hazards

- k = 3 gives δ = 1 (degenerate); k = 4 is the Ising case. Use k = 5 unless asked.
- Do not submit jobs to IBM hardware unless Qiyu asks (queue time, credits).
- Never commit the IBM token. Use `QiskitRuntimeService` saved accounts.
- `FUTURE.md` holds the sl₃ / web-category ideas. Do not pull them into this repo's scope.
