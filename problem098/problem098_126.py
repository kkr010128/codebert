ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

n=ni()
c = [1 if _ == 'R' else 0 for _ in input()]
b = sum(c)

w=0
r=0

for i in range(n):
  if c[i] == 0 and i < b:
    r+=1
  if c[i] == 1 and i >= b:
    w+=1
 

print(max(w,r))


