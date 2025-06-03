N = int(input())

d = {}
for _ in range(N):
  s = input()
  if s in d:
    d[s] += 1
  else:
    d[s] = 1
    
d = {k: v for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True)}

max_count = -1
values = []
for k, v in d.items():
  if max_count < v:
    max_count = v
  if v != max_count:
    break
  values.append(k)

print("\n".join(sorted(values)))