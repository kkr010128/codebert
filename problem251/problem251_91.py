N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = input()
point = [0]*K
flag = ["a"]*K
k = -1
#K本のリストを用意する　剰余系の中で、同じ手が連続するとき、１、３、５、...は別の手に変える
for i in range(N):
  k = (k+1)%K  #mod
  if T[i] == "r":
    if flag[k] == "r":
      flag[k] = "a"
    else:
      flag[k] = "r"
      point[k] += P
  elif T[i] == "s":
    if flag[k] == "s":
      flag[k] = "a"
    else:
      flag[k] = "s"
      point[k] += R
  if T[i] == "p":
    if flag[k] == "p":
      flag[k] = "a"
    else:
      flag[k] = "p"
      point[k] += S
print(sum(point))