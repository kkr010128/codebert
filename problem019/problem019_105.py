n, q = map(int, input().split())
tasks = [(li[0], int(li[1])) for li in [input().split() for _ in range(n)]]

elapsed = 0
while len(tasks):
    name, time = tasks.pop(0)
    if time > q:
        elapsed += q
        tasks.append((name, time - q))
    else:
        elapsed += time
        print('{0} {1}'.format(name, elapsed))