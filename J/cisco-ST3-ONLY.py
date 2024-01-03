from collections import defaultdict
from functools import reduce

N, K = map(int, input().split())
LPF = [None for _ in range(N+1)]
for p in range(2, N+1):
    if LPF[p] is None:
        for k in range(p, N+1, p):
            LPF[k] = p

def prime_factorize(n):
    ans = defaultdict(int)
    while LPF[n] is not None:
        ans[LPF[n]] += 1
        n //= LPF[n]
    return ans

print(sum(reduce(lambda x, y: x*y, [p**(e//K) for p, e in prime_factorize(n).items()], 1) for n in range(1, N+1)))
