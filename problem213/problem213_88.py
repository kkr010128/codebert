n = int(input())
x = list(map(int, input().split()))
sum1 = 100*100**2
for i in range(101):
    sum2 = 0
    for j in range(len(x)):
        sum2 += (x[j] - i)**2
    if sum2 < sum1:
        sum1 = sum2
print(sum1)