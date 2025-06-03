i = list(map(int, input().split()))

time = 0

while (i[0] > 0):
    i[0] -= i[1]
    time += i[2]

print(time)