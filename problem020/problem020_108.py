from _collections import deque

n = int(input())
data_input = []
dlList = deque()
for i in range(n):
    x = input().split()
    if x[0] == 'insert':
        dlList.appendleft(x[1])
    elif x[0] == 'delete':
        if x[1] in dlList:
            dlList.remove(x[1])
        else :
            pass
    elif x[0] == 'deleteFirst':
        dlList.popleft()
    elif x[0] == 'deleteLast':
        dlList.pop()
    else:
        pass

print(' '.join(dlList))