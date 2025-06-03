w = input()
cnt = 0
while(True):
    t = input()
    if t == "END_OF_TEXT":
        break
    t = t.lower().split()
    for i in t:
        if i == w:
            cnt += 1
print(cnt)
