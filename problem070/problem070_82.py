def connected_components(graph):
    seen = set()
    def component(n):
        nodes = set([n])
        while nodes:
            n = nodes.pop()
            seen.add(n)
            nodes |= set(graph[n]) - seen
            yield n
    for n in graph:
        if n not in seen:
            yield component(n)

def print_gen(gen):
    print(len([list(x) for x in gen]) - 1)

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)  # 有向グラフなら消す
graphA = {}
for i in range(n):
    graphA[i] = graph[i]

print_gen(connected_components(graphA))