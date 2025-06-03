from collections import deque
d = deque()
n = int(input())
for i in range(n):
    s = input()
    if s == "deleteFirst":
        d.popleft()
    elif s == "deleteLast":
        d.pop()
    elif s[:6] == "insert":
        d.appendleft(int(s[7:]))
    else:
        delkey = int(s[7:])
        if delkey in d:
            d.remove(delkey)

print(" ".join(map(str,d)))
