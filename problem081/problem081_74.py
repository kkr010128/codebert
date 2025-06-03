
def resolve():
    num = list(map(int, input().split()))
    time = num[0] / num[2]
    if time <= num[1]:
        print("Yes")
    else:
        print("No")
resolve()