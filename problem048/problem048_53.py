
n = input()
m = map(int,raw_input().split())
a = 0
for i in xrange(n):
    a += m[i]

print min(m),max(m),a