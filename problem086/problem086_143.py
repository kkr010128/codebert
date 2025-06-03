N, X, T = list(map(int,input().split()))
if (N%X!=0):
    ans = (N//X + 1) * T
else:
    ans = (N//X) * T
print(ans)
