def main():
    n = int(input())
    a_list = list(map(int, input().split()))

    current = a_list[0]
    answer = 0
    for a in a_list:
        if a < current:
            answer += current - a
        current = max(a, current)
    print(answer)


if __name__ == '__main__':
    main()
