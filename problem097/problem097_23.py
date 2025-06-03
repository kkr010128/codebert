N = int(input())
def resolve():
  a = 7
  for i in range(1,N+1):
    if a % N == 0:
      return i
    a = (a * 10 + 7) % N
  return -1

ans = resolve()
print(ans)