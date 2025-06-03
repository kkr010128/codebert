from collections import deque

n = int(input())
a = deque()

for _ in range(n):
    b = input()
    if b[0] == "i":
        a.appendleft(b[7:])
    elif b[6] == " ":
        try:
            a.remove(b[7:])
        except:
            pass
    elif len(b) > 10:
        a.popleft()
    else:
        a.pop()
print(*a)

