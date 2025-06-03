N,X,T = map(int,input().split())
a = N % X
if a == 0:
    ans = (N//X)*T
else:
    ans = ((N//X)+1)*T
print(ans)