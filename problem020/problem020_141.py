import collections


num_op = int(input())
dllist = collections.deque()

for i in range(0, num_op):
    op = input().split(' ')
    if op[0] == 'insert':
        dllist.appendleft(op[1])
    elif op[0] == 'delete':
        if op[1] in dllist:
            dllist.remove(op[1])
    elif op[0] == 'deleteFirst':
        dllist.popleft()
    elif op[0] == 'deleteLast':
        dllist.pop()

print(' '.join(dllist))
