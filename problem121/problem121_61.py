def main():
    n = int(input())
    alp = 'abcdefghijklmnopqrstuvwxyz'
    answer = ''

    while n >= 1:
        n -= 1
        answer += alp[n % 26]
        n //= 26

    real_answer = ''
    for i in range(1, len(answer) + 1):
        real_answer += answer[-i]

    print(real_answer)


if __name__ == '__main__':
    main()