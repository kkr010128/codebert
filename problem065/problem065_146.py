a = input().lower()
cnt = 0
while 1:
    c = input()
    if c == 'END_OF_TEXT':
        break
    cnt += c.lower().split().count(a)
print(cnt)
