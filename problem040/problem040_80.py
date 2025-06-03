l = map (int, raw_input().split())

if l[0] > l[1]:
    s = l[0]
    l[0] = l[1]
    l[1] = s
if l[2] > l[0]:
    if l[2] < l[1]:
        s = l[1]
        l[1] = l[2]
        l[2] = s
else:
    s = l[2]
    l[2] = l[1]
    l[1] = l[0]
    l[0] = s
print l[0], l[1], l[2]