N, M = list(map(int, input().split()))
sc = []
for i in range(M):
  s, c = list(map(int, input().split()))
  sc.append([s, c])
for i in range(10**N):
  stri = str(i)
  if len(stri) == N:
    for j in range(M):
      k = sc[j][0]
      if not stri[k-1] == str(sc[j][1]):
        break
    else:
      print(i)
      break
else:
  print(-1)