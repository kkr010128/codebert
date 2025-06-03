def gcd(a, b):
    if (a % b) == 0:
        return b
    return gcd(b, a%b)

def lcd(a, b):
    return a * b // gcd(a, b)


while True:
    try:
        nums = list(map(int, input().split()))
        print(gcd(nums[0], nums[1]), lcd(nums[0], nums[1]))

    except EOFError:
        break