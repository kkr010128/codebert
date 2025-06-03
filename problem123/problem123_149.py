def II(): return int(input())
def LI(): return list(map(int, input().split()))
N=II()
a=LI()
A=0
for elem in a:
  A^=elem
ans=[elem^A for elem in a]
print(*ans)