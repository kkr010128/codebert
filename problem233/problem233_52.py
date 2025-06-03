N = int(input())
Pli = list(map(int,input().split()))

a = Pli[0]
res = 1

for i in range(1,N):
  if Pli[i] <= a:
    a = Pli[i]
    res += 1
    
print(res)