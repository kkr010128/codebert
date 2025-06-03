n = input()
A = map(int, raw_input().split())
q = input()
m = map(int, raw_input().split())

def solve(i, m):
 if m == 0:
  return True
 if i >= n or m > sum(A):
  return False
 res = solve(i+1, m) or solve(i+1, m-A[i])
 return res

for j in range(0, q):
 if solve(0, m[j]):
  print 'yes'
 else:
  print 'no'