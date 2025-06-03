ABVW = [map(int, input().split()) for _ in range(2)]
AB, VW = [list(i) for i in zip(*ABVW)]
T = int(input())
 
x = abs(AB[0] - AB[1])
y = (VW[0] - VW[1])*T
if abs(AB[0] - AB[1]) - (VW[0] - VW[1])*T <= 0:
    print("YES")
else:
    print("NO")