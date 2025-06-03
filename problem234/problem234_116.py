#D
N=int(input())
ans=0
D=[[0 for i in range(10)] for j in range(10)]

for i in range(1,10):
    for j in range(1,10):
        for k in range(1,N+1):
            if str(i)==str(k)[0] and str(j)==str(k)[-1]:
                D[i][j]+=1
for i in range(1,10):
    for j in range(1,10):
        ans+=D[i][j]*D[j][i]
print(ans)