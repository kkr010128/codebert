A, B = map(int, input().split())
a = set([])
b = set([])
n = 1
while n**2 <= max(A, B):
  if A%n == 0 and n**2 <= A:
    a.add(n)
    a.add(A//n)
  if B%n == 0 and n**2 <= B:
    b.add(n)
    b.add(B//n)
  n += 1
ab = a & b
ab.discard(1)
ab = list(ab)
answer = 0
for i, n in enumerate(ab):
  prime = True
  for j, m in enumerate(ab):
    if i != j and n%m == 0:
      prime = False
      break
  if prime:
    answer += 1
print(answer+1)
