import sys
readline = sys.stdin.readline

def main():
  N, M, K = map(int, readline().split())
  p = 998244353

  cnt = 0
  c = 1
  for i in range(K+1):
    cnt += c * M * pow(M-1, N-1-i, p)
    cnt %= p
    c *= (N - i - 1) * pow(i+1, p-2, p)
    c %= p
  print(cnt)

if __name__ == '__main__':
  main()