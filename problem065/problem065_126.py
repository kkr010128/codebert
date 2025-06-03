cnt = 0
s = input().lower()
while 1:
    line = input()
    if line == "END_OF_TEXT":
        break
    for w in line.lower().split():
        if w == s:
            cnt+=1
print(cnt)