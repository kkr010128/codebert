import math

n=int(input())
debt=100000
for i in range(n):
    debt=math.ceil((debt*1.05)/1000)*1000
print(int(debt))