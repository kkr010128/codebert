nm = raw_input().split()
n = int(nm[0])
m = int(nm[1])
d = raw_input().split()

c = [0] * 100000
c[0] = 0

for i in range(n):
    min = 100000
    for j in range(m):
        if int(d[j]) < i + 2:
            x = c[i + 1 - int(d[j])]
            if x < min:
                min = x
    c[i + 1] = min + 1

print c[n]