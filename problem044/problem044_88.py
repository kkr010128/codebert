x = map(int, raw_input().split())
flag = 0
for i in range(x[0], x[1]+1):
    if x[2] % i == 0:
        flag += 1
print flag