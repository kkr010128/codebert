n = int(raw_input())
A = map(int, raw_input().split())
d = {}

def soleve(i, m, n):
    if m == 0:
        return True
    if i >= n:
        return False
    if d.has_key((i, m)):
        return d[(i, m)]
    res = soleve(i + 1, m, n) or soleve(i + 1, m - A[i], n)
    d[(i, m)] = res
    return res


q = int(raw_input())
M = map(int, raw_input().split())
for m in M:
    if soleve(0, m, n):
        print 'yes'
    else:
        print 'no'