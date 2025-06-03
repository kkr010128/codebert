# coding: utf-8
n = int(input())
L = list(map(int,input().split()))
l=[]
A=[]
ans=0
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            a=L[i]
            b=L[j]
            c=L[k]
            if a!=b and b!=c and c!=a and a+b>c and b+c>a and c+a>b:
                #print(i+1,j+1,k+1)
                #print(a,b,c)
                ans += 1
#print(L)
#print()
print(ans)