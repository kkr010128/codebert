result = []

def combination(n, x):
    count = 0
    for i in range(1, n + 1):
        for j in range(1,i):
            for k in range(1, j):
                if i + j + k == x:
                    count += 1
    result.append(count)


while True:
    (n, x) = [int(i) for i in input().split()]

    if n == x == 0:
        break

    combination(n, x)

[print(result[x]) for x in range(len(result))]