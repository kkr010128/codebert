W = input()
cnt = 0
while True:
    t = input()
    if t == 'END_OF_TEXT':
        break
    else:
        cnt += t.lower().split().count(W)
print(cnt)

