x = int(input())
s = [0]*x

for i in range(x):
  s[i-1] = input()

l = set (s)
length = len(l)

print(length)