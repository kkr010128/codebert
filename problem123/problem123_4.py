import sys
input=sys.stdin.readline #文字列入力はするな！！

n=int(input())
a=list(map(int,input().split()))

def f(x):
    z=[0]*40
    i=1
    while x>0:
        z[-i]=x%2
        x=x//2
        i+=1
    return z

for i in range(n):
    a[i]=f(a[i])

y=[0]*40
for i in range(40):
    y[i]=sum(a[j][i] for j in range(n))%2
ans=[]
for i in range(n):
    p=0
    for j in range(40):
        if y[-j-1]!=a[i][-j-1]:
            p+=2**j
    ans.append(p)
for i in range(n):
    print(ans[i], end=" ")

