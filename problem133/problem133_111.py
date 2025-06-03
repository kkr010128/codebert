GI = lambda: int(input()); GIS = lambda: map(int, input().split()); LGIS = lambda: list(GIS())

def main():
    a, b = GIS()
    print(a * b)

main()