k,n = map(int,input().split())
lst = list(map(int,input().split()))
m = 0
for i in range(n-1):
  m = max(lst[i+1]-lst[i],m)
  
m = max(m,k+lst[0]-lst[n-1])

print(k-m)