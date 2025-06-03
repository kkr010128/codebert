n = int(input())
a = list(map(int,input().split()))
c = 0

for i in range(n):
    j = i + 1
    while j < n:
        c = c + (a[i] * a[j])
        j += 1

print(c)