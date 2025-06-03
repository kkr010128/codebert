n=int(input())
ans=0
d=5
for i in range(36):
  ans+=n//d//2
  d*=5
print(0 if n%2 else ans)