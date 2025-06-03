from collections import deque
n = int(input())
A = [0]*(n+1)
D = [-1]*(n+1)
DP = [0]*(n+1)
d = deque()
for i in range(n):
    A[i+1] = [int(i) for i in input().split()]
d.append(1)
D[1] = 0
DP[1] = 1
while(len(d)>0):
    tmp = d.pop()
    for i in A[tmp][2:]:
        if not DP[i]:
            D[i] = D[tmp]+1
            DP[i] = 1
            d.appendleft(i)
for i in range(1,n+1):
    tmp = "{} {}".format(i,D[i])
    print(tmp)
