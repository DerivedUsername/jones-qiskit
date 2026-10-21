# Session roadmap

Owner key: **[you]** = hand-written, AI reviews only · **[delegable]** = agents may write.

- [ x] **Session 0 — setup** [delegable]. `.\setup.ps1` runs clean, Bell counts print,
      pytest passes (most tests skip). Create IBM Quantum account, save token with
      `QiskitRuntimeService.save_account(...)`. Push to GitHub.
- [ x] **Session 1 — Temperley–Lieb layer** [you]. `tl.py`. Done when `tests/test_tl.py`
      stops skipping and passes.
- [ ] **Session 2 — braid → unitary** [you]. `braid.py`, path basis on A_{k-1}.
      Done when `tests/test_braid.py` passes (unitarity, braid relations).
- [ ] **Session 3 — exact Jones** [delegable]. `jones_exact.py` via Markov trace,
      with writhe/normalization correction. Done when `tests/test_jones_exact.py`
      passes for unknot, trefoil, figure-eight at k = 5. Record chirality
      convention in CLAUDE.md.
- [ ] **Session 4 — Hadamard test** [you]. `hadamard_test.py`, checked on random
      1-qubit unitaries against numpy.
- [ ] **Session 5 — controlled braid circuits** [you]. `encoding.py`. Fine to start
      with `UnitaryGate`; hand decomposition is an optional upgrade.
- [ ] **Session 6 — simulator pipeline** [you]. `pipeline.py` + notebook with
      convergence plot. **← repo is linkable from here.**
- [ ] **Session 7 — noise** [you, plots delegable]. `AerSimulator.from_backend`,
      Runtime Estimator mitigation options.
- [ ] **Session 8 — hardware** [you]. Trefoil at k = 5 on a real backend. Submit at
      session start; queues are slow.
- [ ] **Sessions 9–10 — README + hygiene** [delegable draft, you edit].
- [ ] **Sessions 11–12 — buffer.**
