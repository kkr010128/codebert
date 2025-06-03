from collections import deque
import sys

input()
lst = deque()

for s in sys.stdin:
    if s[0] == 'i':
        lst.appendleft(s[7:-1])

    else:
        a = s[6]
        if a == ' ':
            try:
                lst.remove(s[7:-1])
            except:
                pass

        elif a == 'F':
                lst.popleft()

        else:
            lst.pop()

print(*lst)
