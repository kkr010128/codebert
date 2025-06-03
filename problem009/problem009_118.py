n = int(input())
v = []
for i in range(n):
    v_i = list(map(int,input().split()))[2:]
    v.append(v_i)
    
d = [-1]*n
d[0]=0
queue = [1]
dis = 1
while len(queue)!=0:
    queue2 = []
    for i in queue:
        for nex in v[i-1]:
            if d[nex-1]==-1:
                d[nex-1]=dis
                queue2.append(nex)
    dis +=1
    queue = queue2

for i in range(n):
    print(i+1,d[i])
