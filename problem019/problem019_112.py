n, q = map(int, input().split())
queue = list()
for i in range(n):
    p = input().split()
    queue.append({"name": p[0], "time": int(p[1])})

t = 0
while len(queue) > 0:
    proc = queue.pop(0)
    if q < proc["time"]:
        proc["time"] -= q
        t += q
        queue.append(proc)
    else:
        t += proc["time"]
        print(proc["name"], t)