n, k, c = map(int, input().split())
c += 1
s = list(input())
a = []
i = 0
while i < len(s) and len(a) < k:
    if s[i] == 'x':
        i += 1
        continue
    a.append(i)
    i += c
b = []
j = len(s)-1
while j > -1 and len(b) < k:
    if s[j] == 'x':
        j -= 1
        continue
    b.append(j)
    j -= c
b = b[::-1]
for i in range(len(a)):
    if a[i] == b[i]:
        print(a[i] + 1)

