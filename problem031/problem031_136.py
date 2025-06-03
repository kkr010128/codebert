import math


def sd(n, students, average):
    rlt = 0
    for i in students:
        rlt += (i - average) ** 2

    rlt = rlt / n
    return math.sqrt(rlt)


if __name__ == '__main__':
    while True:
        n = int(input())
        if not n:
            break
        students = list(map(int, input().split()))

        average = sum(students) / n
        ans = sd(n, students, average)
        print(round(ans, 8))