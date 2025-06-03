N, R = map(int, input().split())
# N回参加、表示レーティングR
if N >= 10:
  rate = R
else:
  rate = R + 100 * (10 - N)
print(rate)