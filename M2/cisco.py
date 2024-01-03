from collections import defaultdict
from dataclasses import dataclass
from enum import Enum
from typing import List

class CutKind(Enum):
    H = 'H'
    V = 'V'

    @staticmethod
    def other(x: 'CutKind') -> 'CutKind':
        if x == CutKind.H:
            return CutKind.V
        elif x == CutKind.V:
            return CutKind.H
        else:
            raise RuntimeError('Impossible case')

@dataclass
class Point:
    i: int
    j: int

    def __eq__(self, other: 'Point') -> bool:
        return self.i == other.i and self.j == other.j

@dataclass
class Cut:
    start: Point
    end: Point

    @property
    def kind(self) -> CutKind:
        if self.start.i == self.end.i:
            return CutKind.H
        elif self.start.j == self.end.j:
            return CutKind.V
        else:
            raise RuntimeError('Non-perpendicular cut found')



def intersect(c1: Cut, c2: Cut) -> bool:
    if c1.kind == c2.kind == CutKind.H:
        if c1.start.i != c2.start.i:
            return False
        l1, r1 = sorted([c1.start.j, c1.end.j])
        l2, r2 = sorted([c2.start.j, c2.end.j])
        return l1 <= r2 and l2 <= r1
    elif c1.kind == c2.kind == CutKind.V:
        if c1.start.j != c2.start.j:
            return False
        u1, b1 = sorted([c1.start.i, c1.end.i])
        u2, b2 = sorted([c2.start.i, c2.end.i])
        return u1 <= b2 and u2 <= b1
    else:
        # WLOG, let c1 be H and c2 be V
        if not (c1.kind == CutKind.H and c2.kind == CutKind.V):
            c1, c2, = c2, c1
        
        l, r = sorted([c1.start.j, c1.end.j])
        u, b = sorted([c2.start.i, c2.end.i])
        return l <= c2.start.j <= r and u <= c1.start.i <= b

rows, cols, k = map(int, input().split())
a = [[int(x) for x in input().split()] for i in range(rows)]
c = [[int(x) for x in input().split()] for i in range(rows)]

best = 10**18
best_at = None
def illustrate(cuts: List[Cut]):
    horizontal_barriers = defaultdict(set)  # i -> set of (j, j+1) barriers
    vertical_barriers = defaultdict(set)    # j -> set of (i, i+1) barriers
    for cut in cuts:
        if cut.kind == CutKind.H:
            horizontal_barriers[cut.start.i] |= set(j for j in range(*sorted([cut.start.j, cut.end.j])))
        elif cut.kind == CutKind.V:
            vertical_barriers[cut.start.j] |= set(i for i in range(*sorted([cut.start.i, cut.end.i])))
        else:
            raise RuntimeError('Impossible case')

    for seed in [0, 1]:
        grid = [[None for j in range(cols)] for i in range(rows)]
        for i in range(rows):
            if 0 in horizontal_barriers[i]:
                seed ^= 1
            curr = seed
            for j in range(cols):
                if i in vertical_barriers[j]:
                    curr ^= 1
                grid[i][j] = curr

        alice = sum(a[i][j] for i in range(rows) for j in range(cols) if grid[i][j] == 0)
        cindy = sum(c[i][j] for i in range(rows) for j in range(cols) if grid[i][j] == 1)
        value = abs(alice - cindy)
        
        global best, best_at
        if value < best:
            best = value
            best_at = grid

def recticut(prior_cuts: List[Cut], curr: Point, kind: CutKind, cuts_left: int):
    if cuts_left == 0:
        illustrate(prior_cuts)
        return
    
    candidates: List[Point]
    if kind == CutKind.H:
        if cuts_left == 1:
            candidates = [Point(curr.i, 0), Point(curr.i, cols)]
        else:
            candidates = [Point(curr.i, j) for j in range(1, cols)]
    elif kind == CutKind.V:
        if cuts_left == 1:
            candidates = [Point(0, curr.j), Point(rows, curr.j)]
        else:
            candidates = [Point(i, curr.j) for i in range(1, rows)]
    else:
        raise RuntimeError('Impossible case')

    for nxt in candidates:
        if curr != nxt:
            next_cut = Cut(curr, nxt)
            if not any(
                intersect(next_cut, prior_cut)
                for prior_cut in prior_cuts[:-1]  # exclude the most recent cut 
            ): 
                recticut(
                    prior_cuts + [next_cut],
                    nxt,
                    CutKind.other(kind),
                    cuts_left-1,
                )

for k_ in range(1, k+1):
    for i in range(1, rows):
        recticut([], Point(i, 0), CutKind.H, k_)
        recticut([], Point(i, cols), CutKind.H, k_)

    for j in range(1, cols):
        recticut([], Point(0, j), CutKind.V, k_)
        recticut([], Point(rows, j), CutKind.V, k_)
    
print(best)
# for row in best_at:
#     print(''.join('A' if c == 0 else 'C' for c in row))
