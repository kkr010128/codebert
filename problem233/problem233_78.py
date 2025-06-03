def resolve():
  n = int(input())
  p = list(map(int, input().split()))
  m = 1000000000
  ans = 0
  for i in range(n):
    if p[i] <= m:
      ans += 1
    m = min(m, p[i])

  print(ans)
  return

if __name__ == "__main__":
  resolve()
