N, k = map(int, input().split())
ans = [1]*(N + 1)
for d in range(2, N + 1):
    if (dk := d**min(k, 50)) > N: break
    for n in range(dk, N + 1, dk): ans[n] = d
print(sum(ans) - 1)
