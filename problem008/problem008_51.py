# coding: utf-8
# Your code here!

n = int(input())
M = []
for i in range(n):
    adj = list(map(int,input().split()))
    if adj[1] == 0:
        M += [[]]
    else:
        M += [adj[2:]]
time = 1
ans = [[j+1,0,0] for j in range(n)] # id d f

while True:
    for i in range(n):
        if ans[i][1] == 0:
            stack = [i]
            ans[i][1] = time
            time += 1
            break
        elif i == n-1:
            for k in range(n):
                print(*ans[k])
            exit()
    while stack != []:
        u = stack[-1]
        if M[u] != []:
            for i in range(len(M[u])):
                v = M[u][0]
                M[u].remove(v)
                if ans[v-1][1] == 0:
                    ans[v-1][1] = time
                    stack.append(v-1)
                    time += 1
                    break
        else:
            stack.pop()
            ans[u][2] = time
            time += 1
     
        
    

