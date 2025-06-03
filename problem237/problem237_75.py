N = int(input())
rob = [] 

for i in range(N):
    x, l = map(int,input().split())
    t = x + l
    rob.append((t,x,l))

rob.sort()
Max = -float("inf")
ans = 0
for i in range(len(rob)): 
    t = rob[i][0]
    x = rob[i][1]
    l = rob[i][2]
    if x-l < Max:
        continue
    else:
        ans += 1
        Max = t
print(ans)