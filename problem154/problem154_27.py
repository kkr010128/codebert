n,k = map(int,input().split())
a = []
for i in range(k):
  d = input()
  a = a+input().split()
a = set(a)
print(n-len(a))
