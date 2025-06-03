n = int(input())


def solve1(n: int) -> str:
    k = 0
    for i in range(len(n)):
        k += int(n[i])

    if k % 9 == 0:
        return "Yes"
    else:
        return "No"


def solve2(n: int) -> str:
    if n % 9 == 0:
        return "Yes"
    else:
        return "No"


print(solve2(n))
