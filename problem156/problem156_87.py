X = int(input())
A = []
for i in range(200):
    A.append(pow(i, 5))
for i in range(200):
    for j in range(200):
        a = abs(A[i] - A[j])
        b = A[i] + A[j]
        if a == X:
            if i <= j:
                B = [j, i]
            else:
                B = [i, j]
            print(' '.join(map(str, B)))
            exit()
        elif b == X:
            B = [i, -j]
            print(' '.join(map(str, B)))
            exit()
