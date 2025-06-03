def main():
  # S = input()[-1:0:-1]
  S = input()[::-1]
  MOD = 2019

  # dp = [0]*(len(S)+1)
  # dp[0] = 0
  dic = [0]*2019
  dic[0] = 1

  ten = 1
  pre = 0
  for i, s in enumerate(S):
    # dp[i] = (dp[i-1] + ten*int(s)) % MOD
    pre = (pre + ten*int(s)) % MOD
    dic[pre] += 1
    ten *= 10
    ten %= MOD

  sum_ = 0
  # for sup in dp:
  #   dic[sup] += 1

  for v in dic:
    sum_ += v*(v-1)//2

  print(sum_)


if(__name__ == '__main__'):
  main()
