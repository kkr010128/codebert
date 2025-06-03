n = int(input())
s = [[] for _ in range(n)]
for i in range(n):
  s[i] = input()
  
s = set(s)
print(len(s))

