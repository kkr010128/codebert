n,k = map(int,input().split())
r,s,p = map(int,input().split())
t = input()

ans = 0
memo = [0]*(n+1)
for i in range(n):
    if t[i] == "r":
        if i-k >= 0 and memo[i-k] == 1:
            pass
        else:
            ans += p
            memo[i] = 1
    elif t[i] == "s":
        if i-k >= 0 and memo[i-k] == 2:
            pass
        else:
            ans += r
            memo[i] = 2
    else:
        if i-k >= 0 and memo[i-k] == 3:
            pass
        else:
            ans += s
            memo[i] = 3
print(ans)