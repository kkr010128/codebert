n = int(input())
a = [int(i) for i in input().split()]
summ = 0
for i in range(n):
    summ += a[i]
a.sort()
print(str(a[0])+" "+str(a[n-1])+" "+str(summ))