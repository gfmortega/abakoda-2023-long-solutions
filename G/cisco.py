r, c = map(int, input().split())
dir = [
    ((0, 1), 'E'),
    ((0, -1), 'W'),
    ((1, 0), 'S'),
    ((-1, 0), 'N'),
]
opposite = {
    'N': 'S',
    'S': 'N',
    'E': 'W',
    'W': 'E',
}

def neighbors(i, j):
    for (di, dj), step in dir:
        ni, nj = i+di, j+dj
        if 0 <= ni < r and 0 <= nj < c:
            yield (ni, nj), step

def move(cmd):
    print(cmd)
    return input()

stack = []
vis = set()
def dfs(curr):
    if curr == (r-1, c-1):
        return True
    for neighbor, step in neighbors(*curr):
        if neighbor not in vis:
            vis.add(neighbor)
            response = move(step)
            if response == 'YAY':
                return True
            elif response == 'SAFE':
                stack.append(step)
                if dfs(neighbor):
                    return True
                assert move(opposite[stack.pop()]) == 'SAFE'
            elif response == 'TRAP':
                for cmd in stack:
                    assert move(cmd) == 'SAFE'
            else:
                raise RuntimeError("invalid response")
    return False

vis.add((0, 0))
if not dfs((0, 0)):
    print('RIGGED')
