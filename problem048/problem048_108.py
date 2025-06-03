i=input()
a=[x for x in map(int, input().split()) ]
a.sort()
print("{0} {1} {2}".format(a[0], a[-1], sum(a)))