n, k = map(int, input().split())
a = [(int(x), i+1) for i, x in enumerate(input().split())]

the_guys = iter(sorted(a, reverse=True))
ans = [None for _ in range(n)]

i = 0
while i < n:
    ans[i] = next(the_guys)[1]
    i += k

for i in range(n):
    if ans[i] is None:
        ans[i] = next(the_guys)[1]

print(*ans)
