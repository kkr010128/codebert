n = int(input())
s, t = input().split()
a = ''
for i, j in zip(s, t):
    a = a + i + j
print(a)