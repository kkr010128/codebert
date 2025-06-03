i = raw_input()
N, A, B = i.split()

N = int(N)
A = int(A)
B = int(B)

if abs(A-B)%2 == 0:
  print int(abs(A-B)/2)
else:
  e = int(min(A-1, N-B))
  d = (B-A+1) // 2
  print e + d