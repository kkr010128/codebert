def II(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

N=II()
a=LI()
A=0
for elem in a:
  A^=elem
ans=[A^elem for elem in a]
print(*ans)