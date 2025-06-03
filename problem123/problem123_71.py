
N = int(input())
A = [int(x) for x in input().split()]

aa = 0
for a in A:
  aa ^= a

print(' '.join([str(aa^a) for a in A]))