import collections
q = collections.deque()
n = int(input())
for i in range(n):
    com = input().split()
    if com[0] == 'insert':
        q.appendleft(int(com[1]))
    elif com[0] == 'delete':
        try:
            q.remove(int(com[1]))
        except:
            pass
    elif com[0] == 'deleteFirst':
        q.popleft()
    elif com[0] == 'deleteLast':
        q.pop()
print(*q)