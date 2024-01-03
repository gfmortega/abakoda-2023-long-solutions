from itertools import permutations
from string import ascii_lowercase

def solve(s):
    cts = {len(s) - s.count(xy): xy for xy in map(''.join, permutations((c for c in ascii_lowercase[::-1] if c not in {*'aeiou'}), 2))}
    return [cts.get(k, 'NO') for k in range(1, len(s) + 1)]

if __name__ == '__main__':
    print(*solve(input()))
