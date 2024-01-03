from heapq import heappush, heappushpop

def cost(V):
    t, l, r, o = 0, [], [], False
    for v in V[:-1]:
        v = (-1)**o * v
        t -= v
        v = -heappushpop(l, -v)
        t += v * 2
        heappush(r, +v)
        l, r, o = r, l, not o
        yield t - o * l[0]

def solve(S, B):
    V = [s - b for s, b in zip(S, B)]
    return [x + y for x, y in zip(cost(V), [*cost(V[::-1])][::-1])]

def main():
    input()
    print(*solve(*([*map(int, input().split())] for a in 'SB')))

if __name__ == '__main__':
    main()
