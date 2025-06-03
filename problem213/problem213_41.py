N=int(input())
X=sorted(list(map(int, input().split())))
 
ans =100000000000
tmp=0
cnt=0
 
for i in range(X[0],X[-1]+1):
    for j in range(len(X)):
        tmp += (X[j]-i)**2
    if ans > tmp:
        ans =tmp
    tmp=0
print(ans)