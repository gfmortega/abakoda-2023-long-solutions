from itertools import chain
dijs = [(i, j) for i in (-1, 0, +1) for j in (-1, 0, +1) if abs(i) + abs(j) == 1]

def solve(grid):
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

def main():
    for cas in range(int(input())):
        r, c = map(int, input().split())
        if res := solve([input() for i in range(r)]):
            print('YES', res, sep='\n')
        else:
            print('NO')

if __name__ == '__main__':
    main()
