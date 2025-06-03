import math
def nor(x,y,p):
    sum = 0
    for i in range(len(x)):
        sum += (abs(x[i]-y[i]))**p
    return sum**(1/p)
def nor_inf(x,y):
    tmp = []
    for i in range(len(x)):
        tmp.append(abs(x[i]-y[i]))
    return max(tmp)
                 
n = int(input())
x = list(map(float,input().split()))
y = list(map(float,input().split()))

print(nor(x,y,1))
print(nor(x,y,2))
print(nor(x,y,3))
print(nor_inf(x,y))