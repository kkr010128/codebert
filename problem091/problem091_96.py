import itertools

N = int(input())
A = list(map(int,input().split()))
A.sort()

Acomb = list(itertools.combinations(A, 3))

ans = 0
for tri in Acomb: 
  if tri[0] < tri[1] and tri[1] < tri[2] and tri[0] + tri[1] > tri[2]:
    ans += 1
print(ans)