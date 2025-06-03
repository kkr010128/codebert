n,k = map(int, input().split())
a = list(map(int, input().split()))
gki = sum(a[0:k])
tmp = gki
rng = k
for i in range(k,n):
  tmp = tmp-a[i-k]+a[i]
  if tmp>gki:
    gki = tmp
    rng = i+1
  
E = 0
for i in a[rng-k:rng]:
  E += (i+1)/2
print(E) 