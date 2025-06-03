import math

data = list(map(int,input().split(" ")))
#0:目標 1:作れる個数 2:一回の時間

n = math.ceil(data[0]/data[1])
#print(n)

print(n * data[2])