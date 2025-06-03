n = int(input())
lst = list(input())

ans = []
for i in range(1000):
    s = str(i).zfill(3)
    pos = 0
    is_exist = True
    for j in range(3):
        if s[j] in lst[pos:]:
            pos += lst[pos:].index(s[j]) + 1
        else:
            is_exist = False
            break
    if is_exist:
        ans.append(s)
print(len(ans))
