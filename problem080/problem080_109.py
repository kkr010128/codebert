n = int(input())
xpy = []
xmy = []
for i in range(n):
    x,y = map(int,input().split())
    xpy.append(x+y)
    xmy.append(x-y)
xpy.sort()
xmy.sort()
print(max(abs(xpy[0]-xpy[-1]),abs(xmy[0]-xmy[-1])))