N=int(input())
A=list(map(int,input().split()))
A1=set(A)
ans="NO"
if len(A)==len(A1):
    ans="YES"
print(ans)