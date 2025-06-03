n = input()
R = []
for i in range(n):
   R.append(int(raw_input()))

maxv = R[1] - R[0]
minv = R[0]

for v in range(1, n):
   if minv > R[v]:
      minv = R[v]
   elif maxv < R[v] - minv:
      maxv = R[v] - minv
print maxv   