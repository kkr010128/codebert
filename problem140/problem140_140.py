t = input()
n = len(t)

res = ''

for i in range(n):
    if t[i] == '?':
        res += 'D'
    else:
        res += t[i]
print(res)