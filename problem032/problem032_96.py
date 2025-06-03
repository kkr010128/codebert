def Dis(X,Y,p):
    D = 0
    for x, y in zip(X, Y):
        dis = abs(x - y) ** p
        D += dis 
    result = D ** (1/p)
    print(result)
def Dis_Che(X, Y):
    print(max(abs(x-y) for x, y in zip(X, Y)))

n = int(input())
X = list(map(int, input().split()))
Y = list(map(int, input().split()))

for p in range(1,4):
    Dis(X, Y, p)
Dis_Che(X,Y)
