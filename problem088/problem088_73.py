n = int(input())
a = list(map(int,input().split()))
x = 0
total = 0


for i in range(n-1):
    if a[i] >= a[i+1]:
        x = a[i] - a[i+1]
        total += x
        a[i+1] = a[i]
        i = i+1
    else:
        total += 0

print(total)