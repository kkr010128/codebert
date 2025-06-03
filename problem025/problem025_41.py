n = int(raw_input())
A = map(int, raw_input().strip().split(' '))
q = int(raw_input())
M = map(int, raw_input().strip().split(' '))

def ans(i, m):
    if m == 0:
        return 1
    if i  >= n or m > sum(A):
        return 0
    res = ans(i + 1, m) or ans(i + 1, m - A[i])
    return res
           
for j in range(0, q):
    if ans(0, M[j]):
        print "yes"
    else:
        print"no"