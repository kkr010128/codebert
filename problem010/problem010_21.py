n = input()
a = map(int, raw_input().split())

for i in range(n):
    key = a[i]
    j = i - 1
    while j >= 0 and a[j] > key:
        a[j + 1] = a[j]
        j -= 1
    a[j + 1] = key
    print(" ".join(map(str, a)))