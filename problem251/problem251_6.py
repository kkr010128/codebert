n, k = map(int, input().split())
r, s, p = map(int, input().split())
t = input()
flag = [False for i in range(n)]
score = {"r":p, "s":r, "p":s}
ans = 0
for i in range(n):
    if i >= k:
        if t[i] == t[i-k]:
            if flag[i-k] == True:
                ans += score[t[i]]
            else:
                flag[i] = True
        else:
            ans += score[t[i]]
    else:
        ans += score[t[i]]
print(ans)