N = int(input())
A = [int(x) for x in input().split()]

c = 0
p = 0
for a in A:
  if p < a:
    p = a
  else:
    c += p - a
    p = max(p, a)
print(c)