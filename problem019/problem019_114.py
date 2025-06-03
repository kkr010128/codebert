from collections import deque
n, q = map(int, input().split())
queue = deque()
for i in range(n):
    name, time = input().split()
    queue.append({"name": name, "time": int(time)})
t = 0
while len(queue) != 0:
    #print([queue[i]["time"] for i in range(len(queue))])
    head = queue.popleft()
    if head["time"] <= q:
        t += head["time"]
        name = head["name"]
        print("{} {}".format(name, t))
    else:
        queue.append({"name": head["name"], "time": head["time"] - q})
        t += q

