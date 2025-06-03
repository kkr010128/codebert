import math
n = int(input())
xlist = list(map(float, input().split()))
ylist = list(map(float, input().split()))
#x, y = [list(map(int, input().split())) for _ in range(2)] 로 한방에 가능
print(sum(abs(xlist[i] - ylist[i]) for i in range(n)))
print(pow(sum(abs(xlist[i] - ylist[i]) ** 2 for i in range(n)),0.5))
print(pow(sum(abs(xlist[i] - ylist[i]) ** 3 for i in range(n)),1/3))
print(max(abs(xlist[i] - ylist[i])for i in range(n)))
