n, m = list(map(int, input().split()))
num = [0 for i in range(n)]

flag = False
for i in range(m):
    s, c = list(map(int, input().split()))

    if (s == 1) and (c == 0) and (n > 1):
        flag = True
    elif num[s-1] == 0:
        num[s-1] = c
    else:
        if num[s-1] != c:
            flag = True

if flag:
    print(-1)
else:
    if (n > 1) and (num[0] == 0):
        num[0] = 1

    print("".join(list(map(str, num))))