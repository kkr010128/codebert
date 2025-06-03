N=int(input())
A=map(int, input().split())
A=list(A)

ans= [0] * len(A)
for i,a in enumerate(A):
    ans[a-1]= i+1
print(' '.join(map(str,ans)))

