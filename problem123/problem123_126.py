n=int(input())
a=list(map(int,input().split()))
x=0
for i in range(n):
    x^=a[i]
for j in range(n):
    print(x^a[j],end=" ")