N = int(input())
a = list(map(int,input().split()))

s = a[0]
count = 1

for i in range(1,N):
  s = min(s,a[i-1])
  if s>=a[i]:
    count+=1
    
print(count)   