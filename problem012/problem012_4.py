c = 0
while True:
    try:
        n = int(input())
    except EOFError:
        break
    c += 1
    for i in range(2, int(n ** 0.5 + 1)):
        if n % i == 0:
            c -= 1
            break
print(c)