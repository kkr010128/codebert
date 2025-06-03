n = int(input())

a = list(map(int,input().split()))
a = sorted(a)

aMax = a[-1]
l = len(a)
count = 0
k = 0
kSet = set()

for i in range(n):
    value = a[i]
    if not(value in kSet):
        if i != 0 and a[i-1] == value:
            count -= 1
            kSet.add(value)
            continue
        count += 1
        j = 2
        k = 0
        while k < aMax:
            k = a[i] * j
            kSet.add(k)
            j += 1

print(count)