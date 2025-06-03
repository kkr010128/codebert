N,u,v = map(int,input().split())
u -= 1
v -= 1

data = [[] for _ in range(N)]

for i in range(N-1):
    A,B = map(int,input().split())
    A -= 1
    B -= 1
    data[A].append(B)
    data[B].append(A)

#print(data)

stack = [[u,u]]
taka_dis = [0] * N
while stack:
    x = stack.pop()
    #print(x)
    for y in data[x[1]]:
        if y == x[0]:
            continue
        else:
            stack.append([x[1],y])
            taka_dis[y] = taka_dis[x[1]] + 1
    #print(stack)

stack = [[v,v]]
aoki_dis = [0] * N
while stack:
    x = stack.pop()
    for y in data[x[1]]:
        if y == x[0]:
            continue
        else:
            stack.append([x[1],y])
            aoki_dis[y] = aoki_dis[x[1]] + 1
    
can = [0] * N

for i in range(N):
    if aoki_dis[i] - taka_dis[i] > 0:
        can[i] = aoki_dis[i]
    else:
        can[i] = 0
#print(aoki_dis)
#print(taka_dis)
#print(can)

print(max(can) -1 )
