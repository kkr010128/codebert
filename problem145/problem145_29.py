from collections import defaultdict, deque

n, m=map(int, input().split())

deq=deque()
dic=defaultdict(list)

for i in range(m):
    a, b = map(int, input().split())
    dic[a].append(b)
    dic[b].append(a)

sign=[-1]*(n+1)
sign[1]=0
for i in dic[1]:
    deq.append(i)
    sign[i]=1

while deq:
    p = deq.popleft()
    for i in dic[p]:
        if sign[i]!=-1:
            continue
        else:
            sign[i]=p
            deq.append(i)

bl = True
for i in range(2, n+1):
    if sign[i]<0:
        bl = False

if bl:
    print("Yes")
    for i in range(2, n+1):
        print(sign[i])
else:
    print("No")