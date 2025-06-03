a = list(input().split())
n = len(a)
s = []
for i in a:
    if i=="+":
        a = s.pop()
        b = s.pop()
        s.append(b + a)
    elif i=="-":
        a = s.pop()
        b = s.pop()
        s.append(b - a)
    elif i=="*":
        a = s.pop()
        b = s.pop()
        s.append(b * a)
    else:
        s.append(int(i))
print(s[0])