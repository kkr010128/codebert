ls = map(int, raw_input().split())
n = 0
for x in xrange(ls[0], ls[1]+1):
    if ls[2]%x==0:
        n+=1

print n