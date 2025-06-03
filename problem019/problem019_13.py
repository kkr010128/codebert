n,q = map(int,input().split())
queue = []
for i in range(n):
    p,t = map(str,(input().split()))
    t = int(t)
    queue.append([p,t])

total_time = 0
while len(queue)  > 0:
    x = queue.pop(0)
    if x[1] > q :
        total_time += q
        x[1] -= q
        queue.append(x)
    else:
        total_time += x[1]
        print(x[0],total_time)