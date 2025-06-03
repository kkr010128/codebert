import collections

a = collections.deque()

for i in range(int(input())):
    b = input()
    # 命令がinsertだった場合、
    if b[0] == 'i':
        # キーxを先頭に追加(数字は文字列bの7文字目以降にある)
        a.appendleft(b[7:])
    # 命令がdeleteだった場合
    elif b[6] == ' ':
        # 命令のキーが含まれる場合そのキーのデータを消すが、なければ何もしない
        try:
            a.remove(b[7:])
        except:
            pass
    # 命令がdeleteFirstだった場合
    elif len(b) > 10:
        a.popleft()
    # 命令がdeleteLastだった場合
    elif len(b) > 6:
        a.pop()

print(*a)




