mod =10**9+7
n=int(input())
if n<2:exit(print(0))
elif n==2:exit(print(2))

ans = 10**n - 9**n*2 + 8**n
ans%=mod
print(ans)