import sys
n = int(input())
input_line = [[int(i) for i in str.split()] for str in sys.stdin.read().splitlines()]
for i in range(n):
    input_line[i] = [] if len(input_line[i]) == 2 else input_line[i][2:]
is_visit = [False] * n
distance = [0] * n
queue = [1]

while len(queue) != 0:
    id = queue.pop(0)
    is_visit[id-1] = True
    for node_id in input_line[id-1]:
        if not is_visit[node_id-1]:
            distance[node_id-1] = distance[id-1] + 1
            queue.append(node_id)
            is_visit[node_id-1] = True

for i in range(n):
    d = distance[i] if is_visit[i] else -1
    print('{0} {1}'.format(i+1, d))




