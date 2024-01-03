R, C, K = [int(x) for x in input().split()]
A = [[int(x) for x in input().split()] for _ in range(R)]
B = [[int(x) for x in input().split()] for _ in range(R)]
#   0 1 2 3 4 5 6
# 0 .............
#   .#.#.#.#.#.#.
# 1 .............
#   .#.#.#.#.#.#.
# 2 .............
#   .#.#.#.#.#.#.
# 3 .............
#   .#.#.#.#.#.#.
# 4 .............
#   .#.#.#.#.#.#.
# 5 .............
#   .#.#.#.#.#.#.
# 6 .............

solutions = []
history = set()
def evaluate(history):
    A2 = [[0 for _ in range(2*C+1)] for _ in range(2*R+1)]
    B2 = [[0 for _ in range(2*C+1)] for _ in range(2*R+1)]
    P = [[" " for _ in range(2*C+1)] for _ in range(2*R+1)]
    for r in range(R):
        for c in range(C):
            A2[2*r+1][2*c+1] = A[r][c]
            B2[2*r+1][2*c+1] = B[r][c]
            P[2*r+1][2*c+1] = "."
    for r,c in history:
        A2[int(2*r)][int(2*c)] = "x"
        B2[int(2*r)][int(2*c)] = "x"
        P[int(2*r)][int(2*c)] = "x"

    def flood(r, c, G, vis):
        if not (0 <= r < 2*R+1 and 0 <= c < 2*C+1):
            return 0
        if vis[r][c]:
            return 0
        vis[r][c] = True
        if G[r][c] == "x":
            return 0
        ans = G[r][c]
        ans += flood(r+1, c, G, vis)
        ans += flood(r-1, c, G, vis)
        ans += flood(r, c+1, G, vis)
        ans += flood(r, c-1, G, vis)
        return ans
    
    total_A = sum(x for row in A for x in row)
    total_B = sum(x for row in B for x in row)
    vis = [[False for _ in range(2*C+2)] for _ in range(2*R+2)]
    partition1_A = flood(0,0,A2,vis)
    vis = [[False for _ in range(2*C+2)] for _ in range(2*R+2)]
    partition1_B = flood(0,0,B2,vis)
    partition2_A = total_A - partition1_A
    partition2_B = total_B - partition1_B

    solutions.append(abs(partition1_A - partition2_B))
    solutions.append(abs(partition1_B - partition2_A))

    # for row in P:
    #     print("".join(row))
    # print(f"alice's partitions: {partition1_A} {partition2_A}")
    # print(f"bob's partitions:   {partition1_B} {partition2_B}")
    # print()

# Given points P1, P2, output the points along the line (P1, P2]
def line(ar, ac, br, bc):
    if ar == br:
        if ac < bc:
            ac += 0.5
        elif bc < ac:
            ac -= 0.5
    elif ac == bc:
        if ar < br:
            ar += 0.5
        elif br < ar:
            ar -= 0.5
    
    r1, r2 = min(ar,br), max(ar, br)
    c1, c2 = min(ac,bc), max(ac, bc)
    S = set()
    if c1 == c2:
        r = float(r1)
        while r <= r2:
            S.add((r, c1))
            r += 0.5
    elif r1 == r2:
        c = float(c1)
        while c <= c2:
            S.add((r1, c))
            c += 0.5
    return S

# (r,c) of head, number of cuts left
def backtrack(hr, hc, ct, type, history, R, C):
    if ct == 0:
        evaluate(history)
        return

    def valid_cut(nr, nc):
        straignt = (hr == nr or hc == nc)
        at_border = (nr == 0 or nr == R or nc == 0 or nc == C)
        in_bounds = (0 <= nr <= R and 0 <= nc <= C)
        if not in_bounds:
            return False
        if not straignt:
            return False
        if ct == 1: # last cut
            if not at_border:
                return False
        else: # not last cut
            if at_border:
                return False
        L = line(hr, hc, nr, nc)
        return len(L.intersection(history)) == 0

    if type == "V":
        for dr in range(-6, 6):
            if dr == 0:
                continue
            nr, nc = hr + dr, hc
            if valid_cut(nr, nc):
                L = line(hr, hc, nr, nc)
                history = history.union(L)
                backtrack(nr, nc, ct-1, "H", history, R, C)
                history = history.difference(L)
    elif type == "H":
        for dc in range(-6, 6):
            if dc == 0:
                continue
            nr, nc = hr, hc + dc
            if valid_cut(nr, nc):
                L = line(hr, hc, nr, nc)
                history = history.union(L)
                backtrack(nr, nc, ct-1, "V", history, R, C)
                history = history.difference(L)

for k in range(1, K+1):
    for c in range(1, C):
        history = {(0,c)}
        backtrack(0, c, k, "V", history, R, C)
        history = {(R,c)}
        backtrack(R, c, k, "V", history, R, C)
    for r in range(1, R):
        history = {(r,0)}
        backtrack(r, 0, k, "H", history, R, C)
        history = {(r,C)}
        backtrack(r, C, k, "H", history, R, C)

print(min(solutions))