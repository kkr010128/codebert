from collections import deque


S = deque(input())
Q = int(input())
reverse_count = 0

for _ in range(Q):
    Query = input().split()
    if Query[0] == "1":
        reverse_count += 1
    else:
        F, C = Query[1], Query[2]
        if F == "1":
            if reverse_count % 2 == 0:
                S.appendleft(C)
            else:
                S.append(C)
        else:
            if reverse_count % 2 == 0:
                S.append(C)
            else:
                S.appendleft(C)

if reverse_count % 2 == 1:
    S.reverse()
print("".join(S))
