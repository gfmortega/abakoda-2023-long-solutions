from heapq import heappush, heappop

def time_to_finish(a, k):
    avail = [0]*k
    for v in a: heappush(avail, heappop(avail) + v)
    return max(avail)

def solve(T, a):
    L, R = 0, len(a) + 1
    while R - L > 1: L, R = (L, M) if time_to_finish(a, M := L + R >> 1) <= T else (M, R)
    return R if R <= len(a) else None

def main():
    for cas in range(int(input())):
        n, T = map(int, input().split())
        if (res := solve(T, [*map(int, input().split())])) is not None:
            print('YES', res, sep='\n')
        else:
            print('NO')

if __name__ == '__main__':
    main()
