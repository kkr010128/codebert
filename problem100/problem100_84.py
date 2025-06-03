def main():
    x = int(input())

    grade = 0
    for i in range(8):
        if (400 + 200 * i) <= x < (400 + 200 * (i + 1)):
            grade = 8 - i

    print(grade)

if __name__ == "__main__":
    main()