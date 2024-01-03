def produce(t, vs):
    if abs(t) <= (s := sum(vs)) and ({*vs} != {1} or (t + s) % 2 == 0) and (len(vs) > 1 or t):
        ds = [None]*len(vs)
        for x in False, True:
            for i in range(len(ds)):
                if (vs[i] == 1) == x:
                    ds[i] = max(-vs[i], vs[i] - s + t) or 1
                    s += ds[i] - vs[i]

        for delt in -1, +1, -2:
            if s == t: break
            for i in range(len(ds)):
                if 1 <= abs(ds[i] + delt) <= vs[i]:
                    ds[i] += delt
                    s += delt
                    break

        return ds

dirn = {
    (-1, 'H'): 'W',
    (+1, 'H'): 'E',
    (-1, 'V'): 'S',
    (+1, 'V'): 'N',
}

def solve(x, y, moves):
    vs, ds = zip(*moves)
    xis = [i for i, d in enumerate(ds) if d == 'H']
    yis = [i for i, d in enumerate(ds) if d == 'V']
    delts = [None]*len(moves)
    for i, delt in zip(xis, produce(-x, [vs[i] for i in xis]) or []): delts[i] = delt
    for i, delt in zip(yis, produce(-y, [vs[i] for i in yis]) or []): delts[i] = delt
    if None not in delts and (x == 0 or xis) and (y == 0 or yis):
        return [(abs(delt), dirn[(delt > 0) - (delt < 0), d]) for delt, d in zip(delts, ds)]

def main():
    def get_move():
        v, d = input().split()
        return int(v), d
    for cas in range(int(input())):
        n, x, y = map(int, input().split())
        if res := solve(x, y, [get_move() for i in range(n)]):
            print('YES')
            for v, d in res: print(v, d)
        else:
            print('NO')

if __name__ == '__main__':
    main()

