def main():
    debt = 100000
    n = int(input())
    for i in range(n):
        debt = debt * 1.05
        if debt % 1000 > 0:
            debt = (debt // 1000 * 1000) + 1000
    print(int(debt))

if __name__ == '__main__':
    main()