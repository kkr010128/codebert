H = int(input())

seen = {}
seen[1] = 1

def count(n):
  if n in seen.keys():
    return seen[n]
  else:
    return 2 * count(n//2) + 1

print(count(H))
