# B - Easy Linear Programming
A,B,C,K = map(int,input().split())
while True:
    ans = 0
    ans += min(A,K)
    K -= min(A,K)
    if K<=0:
        break
    K -= B
    if K<=0:
        break
    ans -= K
    break
print(ans)