n = int(input())
a = [int(x) for x in input().split()]

a.sort()

if n == 1:
    print(1)
    exit()

ans = [1] * (a[n-1]+1)

for i in range(n):
    if i >= 1 and a[i] == a[i-1]:
        ans[a[i]] = 0

    else:
        j = 2
        while j*a[i] <= a[n-1]:
            ans[j*a[i]] = 0
            j += 1


sum = 0

for i in range(n):
    sum += ans[a[i]]


print(sum)
