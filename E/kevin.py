from itertools import combinations
k = int(input())
combs = [*map(frozenset, combinations(range(k), k >> 1))]
print(len(combs))
for b in range(k):
    curr = [i + 1 for i, comb in enumerate(combs) if b not in comb]
    print(len(curr))
    print(*curr, flush=True)
    if not input().startswith('S'): break
else:
    assert False
