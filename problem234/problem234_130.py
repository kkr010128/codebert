n=int(input())
t = [[0 for _ in range(10)] for _ in range(10)]
for i in range(1,n+1):t[int(str(i)[0])][int(str(i)[-1])]+=1
g=0
for i in range(1,10):
    for j in range(1,10):
        g+=t[i][j]*t[j][i]
print(g)