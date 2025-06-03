n = int(input())
x = list(map(float, input().split()))
y = list(map(float, input().split()))

def minc_dis(n, x, y, p):
    sum = 0
    for i in range(n):
        sum = sum + (abs(x[i] - y[i])) ** p
    return sum ** (1/p)

def cheb_dis(n, x, y):
    dis = 0
    for i in range(n):
        dif = abs(x[i] - y[i])
        if dis < dif:
            dis = dif
    return dis

for p in range(1 , 4):
    print(minc_dis(n, x, y, p))

print(cheb_dis(n, x, y))


#print(cheb_dis(2, [1, 2, 3], [2, 0, 4]))
