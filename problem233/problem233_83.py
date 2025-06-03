n = int(input())
p = list(map(int,input().split()))

mini = 10**9
ans =0 

for i in range(n):
  if p[i] <= mini:
    mini = p[i]
    ans += 1
    
print(ans)