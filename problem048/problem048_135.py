# get line input split by space
def getLnInput():
    return input().split()


# ceil(a / b) for a > b
def ceilDivision(a, b):
    return (a - 1) // b + 1


def main():
    getLnInput()
    nums = list(map(int, getLnInput()))
    print(min(nums), max(nums), sum(nums))
    return


main()