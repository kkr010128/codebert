from math import ceil
n=int(input())
money=100000
for i in range(n):
    money=ceil(money*1.05/1000)*1000
print(money)
