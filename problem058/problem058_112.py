while True:
    result = set()
    n, x = map(int, raw_input().split())
    if n == 0 and x == 0:
        break
    else:
        for i in range(1, n + 1):
            for j in range(i, n + 1):
                for k in range(j, n + 1):
                    if i + j + k == x and i != j and j != k and k != i:
                        temp = [i, j, k]
                        sorted(temp)
                        temp = tuple(temp)
                        result.add(temp)
        print(len(result))