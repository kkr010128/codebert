import sys
import collections

N = int(input())

L = collections.deque()
for _ in range(N):
    com = (sys.stdin.readline().rstrip()).split()
    if com[0] == 'insert':
        L.appendleft(int(com[1]))
    elif com[0] == 'delete':
        try:
            L.remove(int(com[1]))
        except:
            pass
    elif com[0] == 'deleteFirst':
        L.popleft()
    elif com[0] == 'deleteLast':
        L.pop()

print(*L)
