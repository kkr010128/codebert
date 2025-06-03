N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
p = -1
q = -1

jun = []
a = [(k+1) for k in range(N)]
def make(now):
  if len(now) == N:
    jun.append(now)
    return 0
  for item in a:
    if item not in now:
      make(now+ [item])
make([])

for k in range(len(jun)):
  if jun[k] == P:
    p = k
  if jun[k] == Q:
    q = k
  if p >=0 and q >=0:
    break
print(abs(p-q))