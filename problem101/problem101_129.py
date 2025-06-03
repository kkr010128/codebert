[A, B, C] = [int(i) for i in input().split()]
K = int(input())


def cal():
    global A, B, C, K
    count = 0
    while A >= B:
        B *= 2
        count += 1
        if K < count:
            return "No"
    while B >= C:
        C *= 2
        count += 1
        if K < count:
            return "No"
    return "Yes"


print(cal())
