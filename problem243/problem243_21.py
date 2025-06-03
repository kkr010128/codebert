N = int(input())
ST = [input().split() for _ in range(N)]
X = input()
flag = False
ans = 0
for i in range(N):
    if flag:
        ans += int(ST[i][1])
    if ST[i][0] == X:
        flag = True
print(ans)