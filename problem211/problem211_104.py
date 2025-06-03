def resolve():
  n, r = map(int, input().split())
  if n >= 10:
    print(r)
    return
  for i in range(10000):
    if i - 100 * (10 - n) == r:
      print(i)
      return
  return

if __name__ == "__main__":
  resolve()
