N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
fact = [1]
for i in range(0,N):
  fact.append(fact[i] * (i+2))
p = 0
q = 0

def number(a):
  res = 0
  global fact
  l = len(a)
  for i in range(l-2):
    res += (a[i] - 1) * fact[l-2-i]
    for j in range(i+1, l-2):
      if a[j] > a[i]:
        a[j] -= 1
  if a[l-1] < a[l-2]:
    res += 2
  else:
    res += 1
  return res
    
p, q = number(P), number(Q)
print(abs(q-p))