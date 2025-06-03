
def main():
  a = list(map(int,input().split()))
  ans = 0
  for i in range(5):
      ans += a[i]
  print(15 - ans)
main()