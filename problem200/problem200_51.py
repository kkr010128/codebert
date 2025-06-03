A, B, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = [list(map(int, input().split())) for _ in range(M)]
buy = [min(a)+min(b)]
for i in range(M):
  C = a[c[i][0]-1]+b[c[i][1]-1]-c[i][2]
  buy.append(C)
print(min(buy))
