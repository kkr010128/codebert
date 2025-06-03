N = int(input())
ab = [list(map(int, input().split())) for i in range(N)]

al = []
bl = []
for a,b in ab:
  al.append(a)
  bl.append(b)
al.sort()
bl.sort()

if N%2 == 0:
  ans = (bl[N//2] + bl[N//2 -1]) - (al[N//2] + al[N//2 -1]) +1
else:
  ans = bl[N//2] - al[N//2] +1
print(ans)