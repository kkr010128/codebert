n = int(input())
a, b = input().split()
s = ""
for i, j in zip(a, b):
  s += i + j
print(s)