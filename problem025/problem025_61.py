def solve(pos, tot, A):
    if tot == 0: return True
    if pos > len(A) - 1: return False

    return solve(pos+1, tot - A[pos], A) or \
           solve(pos+1, tot, A)

n = raw_input()
b = map(int, raw_input().split())
n = raw_input()
t = map(int, raw_input().split())

max = sum(b) + 1
for tt in t:
    print 'yes' if tt < max and True == solve(0, tt, b) else 'no'