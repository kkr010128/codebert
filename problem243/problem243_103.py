N = int(input())

ST = [list(map(str, input().split())) for _ in range(N)]
X = str(input())

ans = 0
flag = False
for s, t in ST:
    if flag:
        ans += int(t)
    else:
        if s == X:
            flag = True

print (ans)