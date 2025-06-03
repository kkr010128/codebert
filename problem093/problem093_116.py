n, k = [int(z) for z in input().strip().split()]
p = [int(z) - 1 for z in input().strip().split()]
c = [int(z) for z in input().strip().split()]
 
visited = [False for _ in range(n)]
cycle = []
for start in range(n):
    if visited[start]:
        continue
    now = start
    route = []
    while not visited[now]:
        visited[now] = True
        route.append(now)
        now = p[now]
    cycle.append(route)
 
min_c = min(c)
max_value = min_c
for route in cycle:
    full_value = sum([c[i] for i in route])
    double_route = route + route
    v = [c[i] for i in double_route]
    max_sum_step = []
    for step in range(1, len(route)):
        s = sum(v[:step])
        max_sum = max(s, min_c)
        for idx in range(step, step + len(route) - 1):
            s += v[idx]
            if idx >= step:
                s -= v[idx - step]
            max_sum = max(s, max_sum)
        max_sum_step.append(max_sum)
    addition = k % len(route)
    if full_value > 0:
        addition_value = 0 if addition == 0 else max(max_sum_step[:addition])
        value1 = int(k / len(route)) * full_value + addition_value
        value2 = (int(k / len(route)) - 1) * full_value + max(max_sum_step)
        value = max(value1, value2)
    else:
        value = max(max_sum_step[:min(k, len(max_sum_step))])
    max_value = max(max_value, value)
print(max_value)