L,R,d = list(map(int, input().split()))

n1 = int(L / d)
if(L % d == 0):
  n1 -= 1
n2 = int(R / d)

print(n2 - n1)