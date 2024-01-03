from itertools import islice, product

def solve(r, c, m, k):
    if r > c: return [*zip(*sol)] if (sol := solve(c, r, m, k)) else None

    if r >= k <= m <= c*k:
        def cells():
            diag = {(i, i) for i in range(k)}
            yield from diag
            yield from {*product(range(k), range(c))} - diag

        grid = [[False]*c for i in range(r)]
        for i, j in islice(cells(), m): grid[i][j] = True
        return grid

def main():
    for cas in range(int(input())):
        if grid := solve(*map(int, input().split())):
            print('YES')
            for row in grid:
                print(''.join('.#'[cell] for cell in row))
        else:
            print('NO')

if __name__ == '__main__':
    main()
