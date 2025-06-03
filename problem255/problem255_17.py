n = int(input())
s, t = input().split(' ')
q = ''

for i in range(n):
    q += s[i]
    q += t[i]

print(q)
