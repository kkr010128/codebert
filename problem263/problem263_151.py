N = int(input())
As = list(map(int, input().split()))
P = 10**9 + 7

rlt = 0
pw = 1
for i in range(61):
  c0 = 0
  c1 = 0
  for j in range(N):
    a = As[j]
    if a % 2 == 0:
      c0 += 1
    else:
      c1 += 1
    As[j] = a//2
  rlt += c0*c1*pw % P
  rlt %= P
  pw *= 2
  
print(rlt)