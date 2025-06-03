
m = 100000
rate = 0.05
n = int(input())
for i in range(n):
    m += m*rate
    x = m%1000
    m -= x
    while(x % 1000 != 0):
        x += 1
    m += x
print(str(int(m)))
