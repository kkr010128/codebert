n, q = (int(x) for x in input().split())
process = [input().split() for _ in range(n)]
time = 0
while process:
    p = process.pop(0)
    if int(p[1]) <= q:
        time += int(p[1])
        print(p[0], time)
    else:
        time += q
        process.append([p[0], int(p[1]) - q])