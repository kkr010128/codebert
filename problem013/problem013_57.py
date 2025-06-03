N = int(raw_input())
min = int(raw_input())
max = int(raw_input())
dif = max - min
if max < min:
    min = max

for i in range(N - 2):
    R = int(raw_input())
    if R - min > dif:
        dif = R - min
    if R < min:
        min = R

print dif