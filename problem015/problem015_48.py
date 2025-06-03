n = int(input())
a = [int(s) for s in input().split(" ")]
cnt = 0

for i in range(n):
    mi = min(a[i:])
    if a[i] > mi:
        j = a[i:].index(mi)+i
        a[i], a[j] = a[j], a[i]
        cnt += 1

print(" ".join([str(i) for i in a]))
print(cnt)