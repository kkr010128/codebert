def area(a,b):
    return a * b

def perimetro(a,b):
    return 2 * (a + b)

def main():
    a,b = map(int,input().split())
    ar = area(a,b)
    pe = perimetro(a,b)
    return ar, pe

ar, pe = main()

print(ar, pe)

