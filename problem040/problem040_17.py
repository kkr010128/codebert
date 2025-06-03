a = list(map(int, input().split()))
for i in range(1,len(a)):
    v = a[i]
    j = i - 1
    while j >= 0 and a[j] > v:
        a[j+1] = a[j]
        j -= 1
    a[j+1] = v

print("{} {} {}".format(a[0],a[1],a[2]))
