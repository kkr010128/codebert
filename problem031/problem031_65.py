import math


result = []
n = int(input())

while n != 0:
    d = list(map(int, input().split()))
    mean = sum(d) / n
    var = [(i - mean) ** 2 for i in d]
    var = math.sqrt(sum(var) / n)
    result.append(var)
    
    n = int(input())

for i in result:
    print(i)
