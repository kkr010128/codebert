def generator(n):
    if n == 1:
        yield [0]
    else:
        for A in generator(n - 1):
            for i in range(max(A) + 2):
                A.append(i)
                yield A
                A.pop()


n = int(input())
for A in generator(n):
    print(''.join([chr(a + 97) for a in A]))