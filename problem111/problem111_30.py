n = int(input())
a = sorted(list(map(int, input().split())))
sum_a = 0
for i in range(n-1):
    j = n-(i+1)//2
    sum_a += a[j-1]
print(sum_a)
