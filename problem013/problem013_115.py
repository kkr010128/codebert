n = input()

R = []
for i in range(n):
    R.append(input())

min_v = R[0]
max_v = -1000000000000
for i in range(1, n):
    temp = R[i] - min_v
    if (temp >= max_v):
        max_v = temp
    temp = R[i]
    if (min_v >= temp):
        min_v = temp
print max_v