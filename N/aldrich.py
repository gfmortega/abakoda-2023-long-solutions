import sys
sys.setrecursionlimit(10**6)

for _ in range(int(input())):
    V, E = [int(x) for x in input().split()]
    v_names = input().split()
    v_name_to_idx = {x : i for i, x in enumerate(v_names)}
    adj_list = {x : [] for x in range(V)}
    for _ in range(E):
        u, v = [v_name_to_idx[x] for x in input().split()]
        adj_list[u].append(v)
        adj_list[v].append(u)

    deg_freq = dict()
    deg_list = {x : [] for x in range(V)}
    for v, Ns in adj_list.items():
        deg = len(Ns)
        deg_freq[deg] = deg_freq.get(deg, 0) + 1
        deg_list[deg].append(v)

    answer = ""
    # # step 1: ensure graph is connected
    vis = [0 for _ in range(V)]
    bfsq = [0]
    while len(bfsq) > 0:
        v = bfsq.pop()
        if vis[v] == 0:
            vis[v] = 1
            for n in adj_list[v]:
                if vis[n] == 0:
                    bfsq.append(n)
    if sum(vis) != V:
        answer = "PRANKED"

    # the operation adds a single 2 to the degree sequence of the graph
    # the original degree sequences are:
    # A : 33211
    # B : 42222
    # C : 22111

    # If the graph is connected and has degree sequence 22...2211,
    # then the graph is necessarily a path graph.
    # Proof:
    # building a chain starting from a deg 1 vertex. this can be adjacent to the other deg 1 vertex or a deg 2 vertex.
    # once the end of the chain is adjacent to the other deg 1 vertex, we're done with this connected component
    # but the graph is connected so it must pass through all deg 2 vertices first
    # 
    # Cindy-graphs need to be a path graph of at least 3 internal vertices.
    def check_C(deg_freq):
        if set(deg_freq.keys()) == {1, 2} and deg_freq[2] >= 3:
            return True
        else:
            return False

    # If the graph is connected and has degree sequence 422...22,
    # then the graph is necessarily a graph with exactly two cycles.
    # Proof:
    # Let the neighbors of the deg 4 vertex be a, b, c, d
    # a b c d must all be deg 2
    # since each of these are deg 2, they must be adjacent to smth else other than the deg 4 vertex
    # since the graph is finite it must loop back to the deg 4 vertex somehow
    # this path saturates two of a b c d, the same logic holds for the other two, this forms two cycles
    # since the graph is connected, the union of the cycles spans all vertices
    def check_B(deg_freq):
        if set(deg_freq.keys()) == {4, 2} and deg_freq[4] == 1:
            return True
        else:
            return False

    # it is sufficient to only check one pivot.
    # suppose a and b are deg 3.
    # further suppose that two of a's branches terminate at b, and the other branch terminates at a leaf
    # it follows that exactly two of b's branches terminate at a. and since there are only two deg 3s and two deg 1s, the third of b's branches terminates at a leaf also
    def check_A(adj_list, deg_freq):
        def walk(prev, curr):
            while len(adj_list[curr]) == 2:
                a, b = adj_list[curr]
                if a == prev:
                    prev, curr = curr, b
                else:
                    prev, curr = curr, a
            return len(adj_list[curr])            

        if set(deg_freq.keys()) == {1, 2, 3} and deg_freq[1] == 2 and deg_freq[3] == 2:
            # pick one of the deg 3 vertices
            pivot = deg_list[3][0]
            terminal_deg = [walk(pivot, x) for x in adj_list[pivot]]
            terminal_deg.sort()
            if terminal_deg == [1, 3, 3]:
                return True
            else:
                return False
        else:
            return False


    if answer == "" and check_C(deg_freq):
        answer = "Cindy"
    if answer == "" and check_B(deg_freq):
        answer = "Bob"
    if answer == "" and check_A(adj_list, deg_freq):
        answer = "Alice"
    if answer == "":
        answer = "PRANKED"
    print(answer)