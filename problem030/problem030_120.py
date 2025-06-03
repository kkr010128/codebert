import math
def main():
    a, b, C = map(int, input().split())
    C /= 180
    C *= math.pi
    
    S = 1 / 2 * a * b * math.sin(C)
    L = math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(C)) + a + b
    h = 2 * S / a
    print(S)
    print(L)
    print(h)


if __name__ == "__main__":
    main()