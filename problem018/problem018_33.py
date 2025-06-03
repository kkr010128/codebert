from operator import *
li = []
for s in input().split():
    if s.isdigit():
        li.append(int(s))
    else:
        b = li.pop()
        a = li.pop()
        li.append({"+":add, "-":sub, "*":mul}[s](a, b))
print(li[-1])

