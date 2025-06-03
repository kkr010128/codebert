import math
n=int(input())
x=list(map(int, input().split()))
y=list(map(int, input().split()))
print(sum([abs(a-b) for (a,b) in zip(x,y)]))
print(math.sqrt(sum([abs(a-b)**2 for (a,b) in zip(x,y)])))
print(math.pow(sum([abs(a-b)**3 for (a,b) in zip(x,y)]), 1/3))
print((max([abs(a-b) for (a,b) in zip(x,y)])))