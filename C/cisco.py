def transpose(grid):
    r = len(grid)
    c = len(grid[0])
    return [
        [grid[i][j] for i in range(r)]
        for j in range(c)
    ]

def solve(r, c, m, k):
    # WLOG suppose r <= c
    if r > c:
        ans = solve(c, r, m, k)
        return None if ans is None else transpose(ans)

    if not (k <= r and k <= m <= k*c):
        return None

    grid = [
        ['.' for j in range(c)]
        for i in range(r)
    ]
    total = 0
    for t in range(k):
        grid[t][t] = '#'
        total += 1

    cells = ((i, j) for i in range(k) for j in range(c))
    while total < m:
        i, j = next(cells)
        if grid[i][j] != '#':
            grid[i][j] = '#'
            total += 1
    
    return grid

if __name__ == '__main__':
    for _ in range(int(input())):
        ans = solve(*map(int, input().split()))
        if ans is None:
            print('IMPOSSIBLE')
        else:
            for row in ans:
                print(''.join(row))
