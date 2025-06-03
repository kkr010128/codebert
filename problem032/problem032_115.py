import math
n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
manhattan = 0
euclid = 0
euclid2 = 0
chebishef = 0

for i, j in zip(x, y):
    tmp = abs(i - j)
    manhattan += tmp
    euclid += tmp * tmp
    euclid2 += tmp * tmp * tmp
    chebishef = max(chebishef, tmp)

print(manhattan)
print(math.sqrt(euclid))
print(math.pow(euclid2, 1 / 3))
print(chebishef)

