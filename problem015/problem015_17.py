n = input()
a = map(int, raw_input().split())

c = 0
for i in range(n):
    mini = i
    for j in range(i, n):
        if a[j] < a[mini]:
            mini = j
    if a[i] != a[mini]:
        a[i], a[mini] = a[mini], a[i]
        c += 1

print(" ".join(map(str, a)))
print(c)