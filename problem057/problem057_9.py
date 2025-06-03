result = []
while True:
    (m, f, r) = [int(i) for i in input().split()]
    sum = m + f

    if m == f == r == -1:
        break

    if m == -1 or f == -1:
        result.append('F')
    elif sum >= 80:
        result.append('A')
    elif sum >= 65:
        result.append('B')
    elif sum >= 50:
        result.append('C')
    elif sum >= 30:
        if r >= 50:
            result.append('C')
        else:
            result.append('D')
    else:
        result.append('F')
    

[print(result[i]) for i in range(len(result))]