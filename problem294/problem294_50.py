n = int(input())
ls = list(map(int, input().split()))
rsw = [0]*1005
for i in ls:
    rsw[i] += 1
for i in range(1,1005):
    rsw[i] = rsw[i-1] + rsw[i]
res = 0
for i in range(n):
    for j in range(i+1,n):
        a = ls[i]
        b = ls[j]
        low = abs(a-b)
        high = a+b
        tmp = rsw[min(high,1004)-1] - rsw[low]
        if low < a < high:
            tmp -= 1
        if low < b < high:
            tmp -= 1
        res += tmp
print(res//3)