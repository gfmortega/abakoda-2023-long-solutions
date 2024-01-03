N, k = map(int, input().split())
ans = [1]*(N + 1)
for d in range(2, int(N**(1/k)*1.1) + 1):
    for n in range(d**k, N + 1, d**k): ans[n] = d
print(sum(ans) - 1)
