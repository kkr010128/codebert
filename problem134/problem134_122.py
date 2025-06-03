N = int(input())
A = list(map(int, input().split()))

# Aに0が含まれていたら、積も0とする
# Aに0が含まれていなければ、順に積を取り、10^18を超えたら終了する
ans = 0
if 0 not in A:
  ans = 1
  for a in A:
    ans *= a
    if ans > 10**18:
      ans = '-1'
      break

print(ans)