from functools import cache
from itertools import chain, combinations, product

dijs = [(i, j) for i in (-1, 0, +1) for j in (-1, 0, +1) if abs(i) + abs(j) == 1]

def cutc(grid):
    r, [c] = len(grid), {*map(len, grid)}
    if len(poss := {grid[i][j]: (i, j) for i, j in chain(
            ((i, j) for i in range(r) for j in (0, c-1)),
            ((i, j) for j in range(c) for i in (0, r-1)),
        )}) != 2: return
    vis = [[False]*c for i in range(r)]
    for v, (i, j) in poss.items():
        vis[i][j] = True
        stak = [(i, j)]
        while stak:
            i, j = stak.pop()
            for di, dj in dijs:
                if 0 <= (ni := i + di) < r and 0 <= (nj := j + dj) < c and grid[ni][nj] == v and not vis[ni][nj]:
                    vis[ni][nj] = True
                    stak.append((ni, nj))
    if not all(all(row) for row in vis): return
    return 1 + sum(
        sum(grid[i + di][j + dj] != grid[i][j] for di in (0, 1) for dj in (0, 1)) & 1
        for i in range(r - 1)
        for j in range(c - 1)
    )

def distinct_consec(*vs):
    return all(x != y for x, y in zip(vs, vs[1:]))

def tree(seqs):
    root = [None]*2
    for seq in seqs:
        node = root
        for v in seq:
            if not node[v]: node[v] = [None]*2
            node = node[v]
    return root

@cache
def cuts(k):
    return [
        (r, c, tree(
            (v for row in g for v in row)
            for g in product(product(range(2), repeat=c), repeat=r)
            if distinct_consec(*g) and distinct_consec(*zip(*g)) and cutc(g) in range(1, k+1))
        )
        for r, c in product(range(1, k+3), repeat=2)
        if r + c <= k + 2
    ]

def sums(r, c, G, s):
    S = [[0]*(c + 1) for i in range(r + 1)]
    for i, j in product(range(r), range(c)):
        S[i + 1][j + 1] = S[i + 1][j] + S[i][j + 1] - S[i][j] + G[i][j] * s
    return S

def merges(G, ispl, jspl):
    return [G[I][J] - G[i][J] - G[I][j] + G[i][j] for i, I in zip(ispl, ispl[1:]) for j, J in zip(jspl, jspl[1:])]

def distrib(ns, Gs, c, d):
    return (min(distrib(cc, Gs, c - 1, d + G[-c]) for G, cc in zip(Gs, ns)) if c else abs(d)) if ns else float('inf')

def solve(r, c, k, A, B):
    A, B = (sums(r, c, G, s) for G, s in ((A, +1), (B, -1)))
    return min(distrib(root, [merges(G, ispl, jspl) for G in (A, B)], pr * pc, 0)
        for pr, pc, root in cuts(k)
        for ispl in ((0, *x, r) for x in combinations(range(1, r), pr - 1))
        for jspl in ((0, *x, c) for x in combinations(range(1, c), pc - 1))
    )

def main():
    r, c, k = map(int, input().split())
    print(solve(r, c, k, *([[*map(int, input().split())] for i in range(r)] for it in range(2))))

if __name__ == '__main__':
    main()
