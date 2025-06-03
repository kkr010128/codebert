#coding: utf-8

n = raw_input()
a = []
for i in range(int(n)):
    l = map(int,raw_input().split())
    a.append(l)

for l in a:
    l = [x * x for x in l]
    l.sort()
    if l[0] + l[1] == l[2]:
        print 'YES'
    else:
        print 'NO'