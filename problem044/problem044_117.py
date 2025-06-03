val = [int(i) for i in input().split()]
result = 0
for i in range(val[0], val[1] + 1):
    if val[2] % i == 0:
        result += 1
print(result)

