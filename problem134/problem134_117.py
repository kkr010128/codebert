n = int(input())
a = list(map(int, input().split()))
a.sort()

def main(a):
  if 0 in a:
    ans = 0
  else:
    ans = 1
    for item in a:
      ans *= item
      if ans > 1000000000000000000:
        ans = -1
        break
  return ans

ans = main(a)
print(ans)
