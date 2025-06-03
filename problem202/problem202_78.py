import math


def main():

    v = list(map(int, input().split()))
    n = v[0]
    a = v[1]
    b = v[2]

    answer = 0
    if n < a:
        answer = n
    elif n < a+b:
        answer = a
    elif a == 0 and b == 0:
        answer = 0
    else:
        answer += math.floor(n / (a+b)) * a
        rest = n % (a+b)
        if rest <= a:
            answer += rest
        else:
            answer += a
    print(answer)


if __name__ == "__main__":
    main()
