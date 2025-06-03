N = int(input())
l = [1] * N
i = 0
d = {1:0,2:0,3:0}
for s in input():
    n = 1
    if s == "G":
        n = 2
    elif s == "B":
        n = 3
    l[i] = n
    d[n] += 1
    i += 1
cnt = d[1] * d[2] * d[3]
for j in range(1,(N - 1) // 2 + 1):
    for k in range(N - (2 * j)):
        if l[k] * l[k+j] * l[k+j+j] == 6:
            cnt -= 1
print(cnt)

