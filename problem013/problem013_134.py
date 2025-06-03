n = int(input())
values = [int(input()) for i in range(n)]

maxv = -999999999
minimum = values[0]

for i in range(1, n):
    if values[i] - minimum > maxv:
        maxv = values[i] - minimum
    if values[i] < minimum:
        minimum = values[i]

print(maxv)