N , D = map(int, input(). split())
Z = [list(map(int, input().split())) for i in range(N)]
total = 0
for point in Z:
    if point[0]**2 + point[1]**2 <= D**2:
        total += 1
    else:
        continue
print(total)
