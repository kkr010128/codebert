# 正整数Xの正約数個数をf(X)とするときの \sum_(K=1)^N {K*f(K)}
# 正整数jの倍数でありN以下のものの総和をg(j)とするときの \sum_(j=1)^N g(j)

N = int(input())
ans = 0
for j in range(1, N+1):
  # Y = N/j とすると g(j) = j+2j+...+Yj = (1+2+...+Y)j = Y(Y+1)/2 *j
  g = (N//j)*(N//j+1)*j//2
  ans += g
print(ans)