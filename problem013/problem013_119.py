#ALDS1_1_D

N = int(input())

min,dif = 10000000000, -10000000000

for i in range(N):
    a = int(input())
    if (a - min) > dif:
        dif = a - min
    if a < min:
        min = a
print(dif)

