def abc178c():
    n = int(input())
    print((pow(10, n) - pow(9, n) - pow(9, n) + pow(8, n)) % (pow(10, 9) + 7))
abc178c()