n, k = map(int, input().split())

a = [0] + list(map(int, input().split()))

cheak = [0] * (2*(10**5) + 1)

point = 1

dev = [1]
flag = 0

for i in range(1, k + 1):
    if cheak[point]:
        loop = i -cheak[point]
        pre_loop = cheak[point]
        flag = 1
        break
    else:
        cheak[point] = i
        point = a[point]
        #dev.append(point)

if flag:
    rest = (k + 1- pre_loop) % loop
    for j in range(rest):
        point = a[point]
        #dev.append(point)

print(point)