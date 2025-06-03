H = int(input())
W = int(input())
N = int(input())

m = max(H,W)
if N%m != 0:
  ans = N/m +1
else:
  ans = N/m

print(int(ans))