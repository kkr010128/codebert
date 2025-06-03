D = 100000
N = int(raw_input())
for i in xrange(N):
    D += D/20
    if D % 1000 > 0:
        D += 1000-D%1000
print D