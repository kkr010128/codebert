#coding: utf-8

n = int(input())
R = []

#input_value?????????
for i in range(n):
    R.append(int(input()))

max_dif = -2000000000
min_value = R[0]

for i in range(1, n):
    max_dif = max(max_dif, R[i] - min_value)
    min_value = min(min_value, R[i])

print(max_dif)