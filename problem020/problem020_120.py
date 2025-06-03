from collections import deque


n = int(input())
a = deque()

for i in range(n):
        s = input()
        if s == 'deleteFirst':
                a.popleft()
        elif s == 'deleteLast':
                a.pop()
        else:     
            s ,t = s.split()
            if s == 'insert':
                a.appendleft(t)
            elif s == 'delete':
                if t in  a:
                    a.remove(t)
        
print(*a, sep = ' ')
