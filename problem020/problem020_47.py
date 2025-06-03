import collections
hoge = collections.deque()
n = int(input())
for _ in range(n):
    commands = input().split()
    if len(commands) == 1:
        if commands[0] == 'deleteFirst':
            hoge.popleft()
        else:
            hoge.pop()
    else:
        com, x = commands
        if com == 'insert':
            hoge.insert(0, x)
        else:
            if x in hoge:
                hoge.remove(x)
print (' '.join(hoge))
