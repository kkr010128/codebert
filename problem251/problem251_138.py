N,K = map(int,input().split())
R,S,P = map(int,input().split())
T = input()
ans = 0
memo = [0 for i in range(N)]
for i in range(N):
    check = T[i]
    if i >= K and T[i-K] == check and memo[i-K] == 0:
        memo[i] = 1
        continue
    if check == "r":
        ans += P
    elif check == "p":
        ans += S
    elif check == "s":
        ans += R
print(ans)