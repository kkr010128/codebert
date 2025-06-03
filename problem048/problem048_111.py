n = int(raw_input())
in_line = raw_input().split()
a = []
for i in in_line:
    a.append(int(i))
a.sort()
print a[0],
print a[len(a)-1],
print sum(a)