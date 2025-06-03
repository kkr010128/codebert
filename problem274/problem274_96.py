n,m = map(int,input().split())
S = list(input())[::-1]
memo = [False]*n
cur = 0
i = 0
ans = []
while i < n:
    for j in range(min(m,n-i),0,-1):
        # print(i,j)
        if S[i+j] == "0":
            ans.append(str(j))
            i += j
            break
        if memo[i+j]:
            ans = -1
            break
        memo[i+j] = True
    if ans == -1:
        break
    # print(S[i:])
print(*ans[::-1]) if ans != -1 else print(-1)