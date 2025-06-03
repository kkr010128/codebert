n, q = list(map(int, input().split()))
que = []
for _ in range(n):
    name, time = input().split()
    que.append([name, int(time)])
    
elapsed_time = 0
while que:
    name, time = que.pop(0)
    dt = min(q, time)
    time -= dt
    elapsed_time += dt
    if time > 0:
        que.append([name, time])
    else:
        print (name, elapsed_time)