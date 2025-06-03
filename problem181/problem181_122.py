k = int(input())
hp = [i for i in range(k+4)]
r, w = 1, 10
while w <= k:
  n = hp[r]
  r += 1
  nm = n % 10
  val = n * 10 + nm
        
  if nm != 0:
    hp[w] = val - 1
    w += 1
  hp[w] = val
  w += 1
  if nm != 9:
    hp[w] = val + 1
    w += 1

print(hp[k])