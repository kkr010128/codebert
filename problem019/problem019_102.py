import collections
n,q = map(int, input().split())
queue = collections.deque(maxlen=100000)

for i in range(n):
    p,t = input().split()
    queue.append([p, int(t)])

time = 0
while queue:
    p,t = queue.popleft()
    if t<=q:
        time += t
        print(p,time)
    else:
        time += q
        queue.append([p,t-q])