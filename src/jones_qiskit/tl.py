"""Temperley–Lieb algebra TL_n(δ).  Session 1 — HUMAN-AUTHORED (see CLAUDE.md).

Suggested representation: a TL diagram on n strands as a perfect matching of the
2n boundary points (0..n-1 on the bottom, n..2n-1 on top), stored as a tuple
`pairs` with pairs[a] = b iff a and b are joined. You may change the internals
freely; the tests only use the functions below. 

Convention: diagrams read bottom to top; compose(a, b) = a∘b (b applied first).
"""


from __future__ import annotations

from dataclasses import dataclass

from math import pi

from math import cos
@dataclass(frozen=True)
class TLDiagram:
    n: int
    pairs: tuple[int, ...]


def delta(k: int) -> float:
    """Loop value δ = 2cos(π/k)."""
    return  2*cos(pi/k)
  


def identity(n: int) -> TLDiagram:
    id = [0]*(2*n)
    for i in range(n):
        id[i] = i+n
        id[i+n] = i
    return TLDiagram(n, tuple(id))
  


def e(i: int, n: int) -> TLDiagram:
    """Generator e_i (1 <= i <= n-1): cup-cap on strands i, i+1."""
    a = [0] * (2*n)
    k = i-1
    a[k] = k+1
    a[k+1] = k
    a[n+k] = k+n+1
    a[k+n+1] = n+k
    for j in range(n):
        if j!= k and j!= n+k and j != k+1 and j != n+k+1:
            a[j] = j+n
            a[j+n] =j
    return TLDiagram(n,tuple(a))
  


def compose(a: TLDiagram, b: TLDiagram) -> tuple[int, TLDiagram]:
    """Stack a on top of b. Return (number of closed loops removed, resulting diagram)."""
    n = int(a.n)
    c = [-1]*(2*n)
    l = 0
    visited = [-1]*n
    """a helper function to find the top or bottom pair of a given bottom point and trace through middle visits"""
    """returns the visited list and the top or bottom pair of the given bottom point"""
    def trace_from_b(i: int, a: TLDiagram, b: TLDiagram) -> int:
        curr = i
        while True:
            if b.pairs[curr] >= n:
                middle  = b.pairs[curr] - n
                visited[middle] = 1
            else: 
                return b.pairs[curr]
            if a.pairs[middle] < n:
                middle = a.pairs[middle]
                visited[middle] = 1
                curr = middle + n
            else:
                return a.pairs[middle]
    def trace_from_a(i: int, a: TLDiagram, b: TLDiagram) -> int:
        curr = i+n
        while True:
            if a.pairs[curr] < n:
                middle  = a.pairs[curr]
                visited[middle] = 1
            else: 
                return a.pairs[curr]
            if b.pairs[middle+n] >= n:
                middle = b.pairs[middle+n] - n
                visited[middle] = 1
                curr = middle
            else:
                return b.pairs[middle+n]
    
    
    
    for i in range(n):
        c[i] = trace_from_b(i,a,b)
        c[i+n] = trace_from_a(i,a,b)   
    for i in range(n):
        if visited[i] == -1:
            curr = i
            while True:
                curr = a.pairs[curr]
                visited[curr]=1
                curr = b.pairs[curr+n] - n
                visited[curr] = 1
                if curr == i:
                    break
            l += 1

    return(l, TLDiagram(n, tuple(c)))
        

        

    
    
        

