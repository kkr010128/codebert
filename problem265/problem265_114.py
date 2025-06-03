#B - Tax Rate 
import math
N = int(input())

result = ':('
for i in range(1,N+1):#+1しないとi=Nの時(1,2,3,4,5,6,7,8,9,10,11,12)が入らない
    if math.floor(i * 1.08) == N:#小数点以下切り捨て
        result = i
print(result)