n = input()
A = map(int, raw_input().split())
q = input()
M = map(int, raw_input().split())

def solve(i, m):
    if m == 0:
        return True
    if n <= i or sum(A) < m:
        return False
    x = (solve(i+1, m) or solve(i+1, m-A[i]))
    return  x
 
for m in M:
    if solve(0, m):
        print "yes"
    else:
        print "no"