from collections import deque
n = int(input())
a = deque()
for i in range(n):
    s = input().split(" ")
    if s[0] == "insert":
        a.appendleft(int(s[1]))
    elif s[0] == "delete":
        if int(s[1]) in a:
            a.remove(int(s[1]))
    elif s[0] == "deleteLast":
        a.pop()
    elif s[0] == "deleteFirst":
        a.popleft()
b = list(a)
for i in range(len(b)):
    if i == len(b)-1:
        print(b[i])
    else:
        print(b[i],end=" ")