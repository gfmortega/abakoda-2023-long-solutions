n, m = map(int, input().split())

def along_a_diagonal(s):
    for i in reversed(range(n)):
        j = s-i
        if 0 <= i < n and 0 <= j < n:
            yield i, j

grid = [[None for j in range(n)] for i in range(n)]
for s in range(2*n-1):
    if s == n-1:
        continue
    row = input()
    for idx, (i, j) in enumerate(along_a_diagonal(s)):
        grid[i][j] = row[idx]

message = []
for _ in range(m):
    code = input()
    i, j = None, None
    for idx, c in enumerate(code):
        if c == '/':
            j = idx
        elif c == '\\':
            i = n-1-idx
    
    assert grid[i][j] != None 
    message.append(grid[i][j])

print(''.join(message))