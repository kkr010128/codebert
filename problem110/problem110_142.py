import copy
H, W, K, = list(map(int, input().split()))
C = [0] * H
for i in range(H):
  C[i] = input()
  C[i] = [1 if(C[i][j] == "#") else 0 for j in range(W)]
h = 2 ** H
w = 2 ** W
ans = 0
for i in range(2 ** H):
  w = 2 ** W
  for j in range(2 ** W):
    D = copy.deepcopy(C)
    for k in range(H):
      for l in range(W):
        if(bin(h)[k + 3] == "1" or bin(w)[l + 3] == "1"):
          D[k][l] = 0
    ans += (sum(map(sum, D)) == K)
    w += 1
  h += 1
print(ans)