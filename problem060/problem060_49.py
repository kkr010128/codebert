def set_matrix (num,matrix):
    for i in xrange(num):
        x = map(int,raw_input().split(" "))
        matrix.append(x)

n,m,l = map(int, raw_input().split())

a = []
b = []
set_matrix(n,a)
set_matrix(m,b)

b_t = list(map(list,zip(*b)))

for i in xrange(n):

    result = []
    for j in xrange(l):
        result.append( sum([x*y for x,y in zip(a[i], b_t[j]) ]))
    print " ".join(map(str,result))