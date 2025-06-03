N=int(input())
A=list(map(int,input().split()))
t=[0]*N
for idx,i in enumerate(A):
    t[i-1]=idx+1

print(*t)