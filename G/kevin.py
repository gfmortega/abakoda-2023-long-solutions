from collections import deque

dijs = {
    (+1, 0): 'S',
    (0, +1): 'E',
    (-1, 0): 'N',
    (0, -1): 'W',
}

def solve(r, c):
    cost = [[(i, j) != (0, 0) for j in range(c)] for i in range(r)]
    while True:
        dist = [[float('inf')]*c for i in range(r)]
        par = [[None]*c for i in range(r)]
        dist[0][0] = 0
        que1, que2 = deque([(0, 0)]), deque()
        while que1 or que2:
            i, j = (que1 or que2).popleft()
            for di, dj in dijs:
                if 0 <= (ni := i + di) < r and 0 <= (nj := j + dj) < c:
                    if cost[ni][nj] <= 1 and dist[ni][nj] > (nd := dist[i][j] + cost[ni][nj]):
                        dist[ni][nj] = nd
                        par[ni][nj] = i, j
                        (que2 if cost[ni][nj] else que1).append((ni, nj))

        if dist[r - 1][c - 1] >= r*c:
            print('RIGGED')
            return

        path = [(r - 1, c - 1)]
        while path[-1] != (0, 0):
            i, j = path[-1]
            path.append(par[i][j])
        path = path[::-1]
        for (i1, j1), (i2, j2) in zip(path, path[1:]):
            print(dijs[i2 - i1, j2 - j1], flush=True)
            if (res := input()) != 'SAFE':
                cost[i2][j2] = float('inf')
                break
            cost[i2][j2] = 0
        else:
            return

solve(*map(int, input().split()))
