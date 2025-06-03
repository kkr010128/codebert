n = int(input())
s = [input().split() for i in range(n)]
b = sum([int(s[i][1]) for i in range(n)])
x = input()
c = 0
for i in range(n):
    c+=int(s[i][1])
    if s[i][0] == x:
        break
print(b-c)