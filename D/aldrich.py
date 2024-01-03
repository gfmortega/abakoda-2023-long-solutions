n, k = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
A = [(A[i], i+1) for i in range(n)]
A.sort()
L = 0
R = n-1
printed = [False for _ in range(n)]
out = []
while True:
    if not printed[R]:
        out.append(A[R][1])
        printed[R] = True
        R -= 1
    else:
        break
    for _ in range(k-1):
        if 0 <= L < n and not printed[L]:
            out.append(A[L][1])
            printed[L] = True
        L += 1
            
print(*out)