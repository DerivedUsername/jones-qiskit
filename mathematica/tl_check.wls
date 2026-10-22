(* ::Package:: *)

(* tl_check.wls — Mathematica cross-validation of the Python TL layer.
   HUMAN-AUTHORED (learning scaffold; see CLAUDE.md).

   Purpose: independently verify, in Mathematica, what src/jones_qiskit/tl.py
   computes in Python — TL relations, the Markov trace, and a known Jones
   value — then a small Groebner-basis demo of the kind used to certify
   solution sets of diagrammatic relations.

   Section 1 is fully worked as a syntax example. Sections 2-4 are exercises:
   each states the goal and the functions to use; fill in the bodies.
   Run: wolframscript -file tl_check.wls   (or open in a notebook and
   evaluate section by section). *)

(* ============================================================ *)
(* Section 1 — WORKED EXAMPLE: TL_3 in the path/matrix model.   *)
(* Represent e_1, e_2 of TL_3(delta) as explicit matrices acting  *)
(* on the 2-dimensional space of length-3 Jones-Wenzl paths,     *)
(* and verify the TL relations symbolically.                     *)
(* ============================================================ *)

delta = 2 Cos[Pi/k];   (* loop value; k symbolic — matches tl.py's delta(k) *)

(* On the standard 2-dim irreducible TL_3 representation one can take: *)
e1 = {{delta, 0}, {0, 0}};
e2 = {{1/delta, Sqrt[1 - 1/delta^2]}, {Sqrt[1 - 1/delta^2], delta - 1/delta}};

check1 = FullSimplify[e1 . e1 - delta e1, Assumptions -> k > 2];
check2 = FullSimplify[e2 . e2 - delta e2, Assumptions -> k > 2];
check3 = FullSimplify[e1 . e2 . e1 - e1, Assumptions -> k > 2];
check4 = FullSimplify[e2 . e1 . e2 - e2, Assumptions -> k > 2];

Print["Section 1 (TL_3 relations): ",
  If[AllTrue[Flatten[{check1, check2, check3, check4}], # === 0 &],
    "all relations hold", "FAILED"]];

(* Things to notice (the whole language in four ideas):
   - delta is a symbolic EXPRESSION in k, not a number; FullSimplify proves
     identities for all k.
   - f[x_] := ... defines functions by pattern matching; x_ matches anything.
   - expr /. {k -> 5} substitutes; N[expr] makes it numeric.
   - Matrix product is . (dot), not *.                                      *)

(* ============================================================ *)
(* Section 2 — EXERCISE: the Markov trace on TL_n.               *)
(* Goal: implement mtrace[word_, n_, k_] taking a word in the    *)
(* e_i (e.g. {1, 2, 1} for e1 e2 e1) and returning the Markov    *)
(* trace of the corresponding TL_n element.                      *)
(* Hint: in the matrix model the Markov trace is a weighted sum  *)
(* of diagonal entries with weights given by quantum dimensions  *)
(* [m+1]_q of the through-strand sectors; start with n = 3 where *)
(* you can hand-check against tl.py's compose + loop counting.   *)
(* Useful: Tr, Dot, Fold, Table.                                 *)
(* ============================================================ *)

(* mtrace[word_, n_, k_] := ... *)

(* ============================================================ *)
(* Section 3 — EXERCISE: a known Jones value.                    *)
(* Goal: compute the Jones polynomial of the trefoil from the    *)
(* Markov trace of its braid word (sigma_1^3 in B_2, or use B_3) *)
(* and check it against reference.py's value after the standard  *)
(* variable substitution.                                        *)
(* Hint: the braid generator acts as A + A^-1 e_i (Kauffman);    *)
(* write sigma[i_] := A IdentityMatrix[2] + A^-1 ei, build the    *)
(* word with Dot, apply Section 2's trace, then the writhe       *)
(* normalization. Compare with V(trefoil) = -t^-4 + t^-3 + t^-1  *)
(* under t = A^-4.                                               *)
(* ============================================================ *)

(* jonesTrefoil = ... *)

(* ============================================================ *)
(* Section 4 — EXERCISE: Groebner bases on a toy relation set.   *)
(* Goal: see how GroebnerBasis certifies the SHAPE of a solution *)
(* set, the way the sl3 verification pipeline does.              *)
(* Take unknowns {x, y, c} and impose toy "diagrammatic"         *)
(* relations, e.g.                                               *)
(*   polys = {x y - c, x^2 - x, y^2 (c - 1)};                     *)
(* 1. GroebnerBasis[polys, {x, y, c}]  — read off the triangular *)
(*    structure.                                                  *)
(* 2. Solve[polys == 0, {x, y}, ...]  — which components are a   *)
(*    curve in c (a "c-line") and which are isolated points?     *)
(* 3. Append a relation that makes the system inconsistent and   *)
(*    watch the basis become {1}.                                *)
(* Useful: GroebnerBasis, Solve, Reduce, Eliminate.              *)
(* ============================================================ *)

(* gb = GroebnerBasis[...] *)
