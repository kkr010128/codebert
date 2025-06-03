s = input()
p = input()
for e, i in enumerate(s):
    if i == p[0]:
        temp = s[e:] + s[:e]
        if p in temp:
            print('Yes')
            break
else:
    print('No')