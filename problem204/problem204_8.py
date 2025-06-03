from collections import deque
S = input()
Q = int(input())
a = deque([])
for i in S:
    a.append(i)

# is_reverse: 反転しているか
is_reverse = False
for i in range(Q):
    query = input().split()
    if query[0] == "1":
        is_reverse = not is_reverse
    else:
        if query[1] == "1":
            if is_reverse:
                a.append(query[2])
            else:
                a.appendleft(query[2])
        else:
            if is_reverse:
                a.appendleft(query[2])
            else:
                a.append(query[2])
if is_reverse:
    while len(a)>0:
        print(a.pop(), end="")
else:
    while len(a)>0:
        print(a.popleft(), end="")
print()