N,K = map(int,input().split())
A = list(map(int, input().split()))
F = list(map(int, input().split()))

if sum(A) <= K:
  print(0)
  exit()

A.sort()
F.sort(reverse=True)

def check(x):
  k = 0
  for a,f in zip(A, F):
    k += max(0, a-(x//f))

  return k <= K

# AをX以下にできるか？?
ng,ok = 0, 10**18+1
while ok-ng > 1:
  x = (ok+ng)//2
  if check(x):
    ok = x
  else:
    ng = x

print(ok)
