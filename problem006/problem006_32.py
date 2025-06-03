from math import ceil
n = int(input())
dept = 100000
for i in range(n):
    dept += dept*0.05
    dept = int(int(ceil(dept/1000)*1000))
print(dept)