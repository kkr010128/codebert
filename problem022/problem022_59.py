n = int(input())
s = list(map(int, input().split()))

q = int(input())
t = list(map(int, input().split()))

count = 0

for i in range(q):
    s.append(t[i])
    j = 0
    while t[i] != s[j]:
        j += 1
    if j != n:
        count += 1
    del s[n]
print(count)
