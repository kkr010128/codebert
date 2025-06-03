N = int(input())
A = list(map(int, input().split()))
B = [0]*60
mod = 10 ** 9 + 7

for x in A:
  temp = bin(x)[2:]
  for i in range(len(temp)):
    if temp[-1-i] == "1":
      B[i] += 1

ans = 0

for i in range(60):
  ans += (N-B[i])*B[i]*pow(2, i, mod)
  ans %= mod

print(ans)
