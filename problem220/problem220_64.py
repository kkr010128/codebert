s1, s2 = input().split()
n1, n2 = map(int, input().split())
u = input()
if u == s1:
  n1 -= 1
else:
  n2 -= 1
print(n1, n2)