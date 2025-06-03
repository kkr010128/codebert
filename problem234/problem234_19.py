N=int(input())
l = [[] for _ in range(9)]
for i in range(0,9):
    for j in range(0,9):
        l[i].append(0)
for i in range(N+1):
    if (int(str(i)[0])!=0 and int(str(i)[-1])!=0):
        l[int(str(i)[0])-1][int(str(i)[-1])-1]+=1
t=0
for i in range(9):
    for j in range(9):
        t+=l[i][j]*l[j][i]
print(t)