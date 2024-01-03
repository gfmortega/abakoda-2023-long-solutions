from itertools import permutations
n, k = map(int, input().split())
conf = [[['|']*n for j in range(n)] for i in range(n)]
for i, j in permutations(range(n), 2): conf[i][j][i], conf[i][j][j] = '/\\'
lett = [[None]*n for i in range(n)]
for i in range(n - 1):
    for j, c in enumerate(input()): lett[j][n - 1 - i + j] = c
for i in range(n - 1)[::-1]:
    for j, c in enumerate(input()): lett[n - 1 - i + j][j] = c
dec = dict(zip((''.join(c) for c in sum(conf, [])), sum(lett, [])))
print(''.join(dec[input()] for it in range(k)))
