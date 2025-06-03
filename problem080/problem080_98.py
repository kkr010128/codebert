N = int(input())
p = [list(map(int,input().split())) for _ in range(N)]

z = []
w = []

for i in range(N):
  z.append(p[i][0] + p[i][1])
  w.append(p[i][0] - p[i][1])

print(max(max(z)-min(z),max(w)-min(w)))