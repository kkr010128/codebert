#coding:utf-8

i = input()
q = []
for n in range(i):
    l = map(int, raw_input(). split())
    a = min(l)
    l.remove(min(l))
    b = min(l)
    c = max(l)
    if a ** 2 + b ** 2 == c ** 2:
        q.append("YES")
    else:
        q.append("NO")

for s in xrange(len(q)):
    print(q[0])
    q.pop(0)