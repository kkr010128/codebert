# ABC 148 D

N=int(input())
A=list(map(int,input().split()))

K=1
dest=0
for a in A:
    if a==K:
        K+=1
    else:
        dest+=1
print(dest if K>1 else -1)