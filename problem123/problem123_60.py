n = int(input())
a = list(map(int, input().split()))

def nim(x):
  bx = [format(i,'030b') for i in x]
  bz = ''.join([str( sum([int(bx[xi][i]) for xi in range(len(x))]) % 2)  for i in range(30)])
  return int(bz, 2)

nima = nim(a)
ans = [ str(nim([nima,aa])) for aa in a ]
print(' '.join(ans) )