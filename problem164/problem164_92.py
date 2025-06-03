import math

A, B, C, D = map(int, input().split())

#on which turn do they die
takahashi = math.ceil(A / D)
aoki = math.ceil(C / B)
#print(takahashi)
#print(aoki)

if takahashi >= aoki:
    print("Yes")
else:
    print("No")
