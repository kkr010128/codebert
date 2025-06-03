l =  list(map(int, input().split()))
r = []
for i in range(0, 2, 1):
  for j in range(2, 4, 1):
    r.append(l[i] * l[j])

print(max(r))