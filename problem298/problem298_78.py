n,k=map(int,input().split())
n=list(map(int,input().split()))
a=0
for i in n:
    if i>=k:
        a+=1
print(a)
