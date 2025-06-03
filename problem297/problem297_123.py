def main():
    n = int(input())
    t = (n+1) // 2
    if n == 1:
        print(1)
    elif n % 2 == 0:
        print(0.5)
    else:
        print(t*1.0 / n)
main()