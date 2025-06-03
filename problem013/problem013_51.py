n=int(input())
num=[int(input()) for i in range(n)]

maxv=num[1]-num[0]
minv=num[0]

for j,n in enumerate(num[1:]):
    maxv=max(maxv,n-minv)
    minv=min(minv,num[j+1])

print(maxv)