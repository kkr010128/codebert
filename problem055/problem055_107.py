house_info = [[[0 for i in xrange(10)]for j in xrange(3)]for k in xrange(4)]

n = input()

for i in xrange(n):
    b,f,r,v=map(int,raw_input().split())
    house_info[b-1][f-1][r-1] += v
    
for i in xrange(4):
    for j in xrange(3):
        result = " " + " ".join(map(str,house_info[i][j]))
        print result
    if i < 3:
        print "####################"