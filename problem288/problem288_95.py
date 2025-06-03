n=int(input())
ans = n
for i in range(1,int(n**0.5)+2):
  if n % i == 0:
    ans = min(ans,(i-1)+(n//i-1))
print(ans)