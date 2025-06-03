def g(s):
    a, b, c = list(map(int, s.split()))
    for i in range(a, b+1):
        if c % i == 0:
            yield 1

print(sum(g(input())))