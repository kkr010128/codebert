count = 0


N = int(input())
P = "".join(list(map(str, input().split())))
Q = "".join(list(map(str, input().split())))


ans = []

def dfs(curr, p, q, n):
    if len(curr) == n:
        global count
        count+=1
        if curr == p:
            ans.append(count)
        if curr == q:
            ans.append(count)

        return 

    for i in range(1, n+1):
        if str(i) not in curr:
            dfs(curr + str(i), p, q, n)

for i in range(1, N + 1):
    dfs(str(i), P, Q, N)

print(abs(ans[0]-ans[1]))


