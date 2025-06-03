#coding: UTF-8
a = raw_input()
l = map(int, raw_input().split())


l.sort()
x =l[0]


l.reverse()
y = l[0]

z = sum(l)


print "%d %d %d" %(x, y, z)