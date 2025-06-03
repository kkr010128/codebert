N = int(input())

ans = (N * 100 + 99) // 108

if N==int(ans*1.08):
  print(ans)
else:
  print(':(')
