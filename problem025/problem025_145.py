n= int(input())
A = list(map(int, input().split()))
q = int(input())
Mi = map(int, input().split())
PS={}
def solve(i,m):
 if m == 0:
  return True
 if (i,m) in PS:
  return PS[(i,m)]
 if i >= n:
  return False
 res = solve(i+1, m) or solve(i + 1, m - A[i])
 PS[(i,m)] = res
 return res

for m in Mi:
 if solve(0, m):
  print("yes")
 else:
  print("no")