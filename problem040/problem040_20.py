#coding:utf-8

l = map(int, raw_input(). split())
i = min(l)
l.remove(min(l))
n = min(l)
l.remove(min(l))
m = min(l)
print("{0} {1} {2}". format(i, n, m))