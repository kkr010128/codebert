n = int(input())
a = list(map(int, input().split()))
q = int(input())
sums = sum(a)
d = {}

for i in a:
  if i in d:
    d[i] += 1
  else:
    d[i] = 1

for i in range(q):
    b,c = map(int, input().split())
    if b in d:
        sums += d[b]*(c-b)
        if c in d:
          d[c] += d[b]
        else:
          d[c] = d[b]
        d[b] = 0
    print(sums)