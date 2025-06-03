def main():
    a, b = input().split()
    a = int(a)
    b = round(float(b) * 100)
    print(int(a * b // 100))


if __name__ == "__main__":
    main()
