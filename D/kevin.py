def solve(n, k, a):
    b = [None]*n
    for i, j in zip((i for r in range(k) for i in range(r, n, k)), sorted(range(n), key=lambda i: a[i], reverse=True)):
        b[i] = j
    return b

if __name__ == '__main__':
    print(*(i + 1 for i in solve(*map(int, input().split()), [*map(int, input().split())])))
