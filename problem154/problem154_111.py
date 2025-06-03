n,k = map(int, input().split())
setn = {x for x in range(1,n+1)}
setd = set()
for i in range(k):
  d = int(input())
  setd |= set(map(int, input().split()))
print(len(setn - setd))