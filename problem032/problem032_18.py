n = int(input())
x = input().split()
y = input().split()
import math
for i in range(4):
    D = 0
    for j in range(n):
        if i != 3:
            D = D + math.pow(math.fabs(int(x[j]) - int(y[j])),i+1)
        else:
            compare = math.fabs(int(x[j]) - int(y[j]))
            if D < compare:
                D = compare
    if i != 3:
        print('{0:.6f}'.format(math.pow(D,1/(i+1))))
    else:
        print('{0:.6f}'.format(D))
