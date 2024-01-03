def graph_data(adj):
    return *sorted(len(adj[i]) for i in adj), *sorted(len(adj[i]) + len(adj[j]) for i in adj for j in adj[i])

def adj_from(nodes, edges):
    adj = {node: set() for node in nodes}
    for i, j in edges:
        adj[i].add(j)
        adj[j].add(i)
    return adj

nodes = range(5)
owners = {graph_data(adj_from(nodes, (*zip(nodes, nodes[1:]), *extras))): name
    for name, extras in [
        ('Alice', [(1, 3)]),
        ('Bob',   [(0, 2), (2, 4)]),
        ('Cindy', []),
    ]}

def solve(nodes, edges):
    adj = adj_from(nodes, edges)
    for i in (i for i in nodes if len(adj[i]) == 2):
        if len(adj) <= 5: break
        a, b = adj[i]
        if b not in adj[a]:
            adj.pop(i)
            adj[a].remove(i)
            adj[b].remove(i)
            adj[a].add(b)
            adj[b].add(a)

    if len(adj) <= 5: return owners.get(graph_data(adj))

def main():
    for cas in range(int(input())):
        n, e = map(int, input().split())
        print(solve([*input().split()], [(*input().split(),) for ee in range(e)]) or 'PRANKED')

if __name__ == '__main__':
    main()
