a, b, c = map(int,raw_input().split())
count = 0
for x in xrange(a,b+1):
    if c%x == 0:
        count+=1
print count