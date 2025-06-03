N = int(input())
ans = N // 1000

if N % 1000 == 0:
  print(0)
else:
  print(1000*(ans+1) - N)