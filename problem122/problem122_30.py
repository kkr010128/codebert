n = int(input())
a = list(map(int, input().split()))
q = int(input())

m = 10**5+1
nums = [0]*m
ans = 0
for i in a:
  nums[i] += 1
  ans += i
  
for _ in range(q):
  b,c = map(int, input().split())
  ans -= b*nums[b]
  ans += c*nums[b]
  nums[c] += nums[b]
  nums[b] = 0
  print(ans)