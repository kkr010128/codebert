w = input()
cnt = 0
while(True):
    t = input()
    if t == "END_OF_TEXT":
        break
    t = t.lower()
    tlist = t.split()
    for i in tlist:
        if i == w:
            cnt += 1
print(cnt)
