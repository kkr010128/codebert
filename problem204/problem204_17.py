from collections import deque
S = input()
Q = int(input())
Query = []

for i in range(Q):
    Query.append(list(input().split()))


turning = 1
# 1なら正常　-1なら反転
ans = deque(S)
for i in Query:
    if i[0] == "1":
        turning *= -1
    else:
        if i[1] == "1":
            if turning == 1:
                ans.appendleft(i[2])
            else:
                ans.append(i[2])
        else:
            if turning == 1:
                ans.append(i[2])
            else:
                ans.appendleft(i[2])


print("".join(list(ans)) if turning == 1 else "".join(list(ans)[::-1]))
