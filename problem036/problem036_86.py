def rectangle(a, b):
    S = a * b
    L = a*2 + b*2
    print(S, L)

a, b =[int(x) for x in input().split()]

rectangle(a, b)