def main():
    x, y = input().split()
    answer = 0
    prize = {"1": 300000, "2": 200000, "3": 100000}
    if x in prize:
        answer += prize[x]
    if y in prize:
        answer += prize[y]
    if x == y == "1":
        answer += 400000
    print(answer)


if __name__ == '__main__':
    main()

