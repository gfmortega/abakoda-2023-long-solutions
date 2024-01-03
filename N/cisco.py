from collections import defaultdict
from itertools import permutations

def contract(adj):  # remove all u--x--v edges
    degree2 = [x for x in adj.keys() if sum(adj[x].values()) == 2]
    for x in degree2:
        if len(adj[x].keys()) == 1:
            u, = adj[x].keys()
            if u == x:
                continue
            adj[u][u] += 2
            del adj[u][x]
        else:
            u, v = adj[x].keys()
            adj[u][v] += 1
            del adj[u][x]
            adj[v][u] += 1
            del adj[v][x]

        del adj[x]

def graph_isomorphism(adj_G, adj_H):
    G_nodes = list(adj_G.keys())
    H_nodes = list(adj_H.keys())
    if len(G_nodes) != len(H_nodes):
        return False
    n = len(G_nodes)
    return any(
        all(
            (
                adj_G[G_nodes[i]][G_nodes[j]] ==
                adj_H[H_nodes[p[i]]][H_nodes[p[j]]]
            )
            for i in range(n)
            for j in range(n)
        )
        for p in permutations(range(n))
    )
    

alice = {
    0: defaultdict(int, {
        1: 1,
    }),
    1: defaultdict(int, {
        0: 1,
        2: 2,
    }),
    2: defaultdict(int, {
        1: 2,
        3: 1,
    }),
    3: defaultdict(int, {
        2: 1,
    }),
}
bob = {
    0: defaultdict(int, {
        0: 4,
    }),
}
cindy = {
    0: defaultdict(int, {
        1: 1,
    }),
    1: defaultdict(int, {
        0: 1,
    }),
}

def solve(pc_names, edge_list):
    if len(pc_names) < 5:
        return 'PRANKED'

    adj = {
        pc_name: defaultdict(int)
        for pc_name in pc_names
    }
    for u, v in edge_list:
        adj[u][v] += 1
        adj[v][u] += 1

    contract(adj)
    possible = [
        name
        for name, candidate_graph in [
            ('Alice', alice),
            ('Bob', bob),
            ('Cindy', cindy),
        ]
        if graph_isomorphism(adj, candidate_graph)
    ]
    if possible:
        return ' '.join(possible)
    else:
        return 'PRANKED'


if __name__ == '__main__':
    for _ in range(int(input())):
        n, m = map(int, input().split())
        pc_names = input().split()
        edge_list = [input().split() for _ in range(m)]
        print(solve(pc_names, edge_list))    
