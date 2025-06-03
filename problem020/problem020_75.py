n = int(input())
import collections
d = collections.deque([])
for _ in range(n):
    s = input().split()
    if s[0] == "deleteFirst":
        d.popleft()
    elif s[0] == "deleteLast":
        d.pop()
    elif s[0] == "insert":
        d.appendleft(s[1])
    else:
        try:
            d.remove(s[1])
        except:
            pass
print(" ".join(d))

