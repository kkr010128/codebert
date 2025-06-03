N = int(input())
A = [int(i) for i in input().split()]
ans = 0
for i,a in enumerate(A):
  idx = i+1
  if a%2 == 1 and idx%2 == 1:
    ans += 1
print(ans)