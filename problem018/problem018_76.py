s = []
for e in input().split():
    s.append(e if e.isdigit() else str(eval(s.pop(-2)+e+s.pop())))
print(*s)