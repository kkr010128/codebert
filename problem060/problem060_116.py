def show2dlist(nlist,r,c):
    for x in xrange(0,r):
        nlist[x] = map(str,nlist[x])
        ans = " ".join(nlist[x])
        print ans
# input
n,m,l = map(int,raw_input().split())
a_matrix = [[0 for x in xrange(m)] for y in xrange(n)]
b_matrix = [[0 for x in xrange(l)] for y in xrange(m)]
for x in xrange(n):
    a_matrix[x] = map(int,raw_input().split())
for x in xrange(m):
    b_matrix[x] = map(int,raw_input().split())

c_matrix = [[0 for x in xrange(l)] for y in xrange(n)]

# calc
for ni in xrange(n):
    for li in xrange(l):
        for mi in xrange(m):
            c_matrix[ni][li] += a_matrix[ni][mi] * b_matrix[mi][li]

# show result
show2dlist(c_matrix,n,l)