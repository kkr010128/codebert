#10^18こえたら-1
n = int(input())
Arr = list(map(int, input().split( )))
Arr = sorted(Arr)
if Arr[0] == 0:
  print(0)
  exit()
s = 1
for i in range(n):
  s *= Arr[i]
  if s > 10**18:
    print(-1)
    exit()
print(s)