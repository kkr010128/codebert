t = input().lower()
cnt = 0
while True:
    w = input()
    if w == 'END_OF_TEXT': break
    cnt += len(list(filter(lambda x: x == t, [v.lower() for v in w.split(' ')])))
print(cnt)
