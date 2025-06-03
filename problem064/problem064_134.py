s = raw_input()
p = raw_input()
idx = []
for i in range(0,len(s)):
    if s[i] == p[0]:
        idx.append(i)
for i in idx:
    for j in range(0,len(p)):
        if p[j] == s[(i+j)%len(s)]:
            continue
        else:
            break
    else:
        print 'Yes'
        break
else:
    print 'No'