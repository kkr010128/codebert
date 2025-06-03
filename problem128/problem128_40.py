x, n = map(int,input().split())

p = list(map(int,input().split()))

d =100
num = 0

if n == 0:
    num = x
else:
    for i in range(102):
        if i not in p:
            d_temp = abs(x-i)
            if d_temp < d:
                d = d_temp
                num = i
print(num)