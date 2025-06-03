n1 = input()
A = map(int, raw_input().split())

n2 = input()
q = map(int, raw_input().split())

list = set()

def solve(i,m):
 if m == 0:
  return True
 if i >= n1 or m > sum(A):
  return False
 res = solve(i+1,m) or solve(i+1,m-A[i])
 return res

for m in q:
 if solve(0,m):
  print "yes"
 else:
  print "no"