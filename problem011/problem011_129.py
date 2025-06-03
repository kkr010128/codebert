#coding:utf-8
#1_1_B
def gcd(x, y):
    while x%y != 0:
        x, y = y, x%y
    return y

x, y = map(int, input().split())
print(gcd(x, y))