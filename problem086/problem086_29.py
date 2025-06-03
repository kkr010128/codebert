def resolve():
    num = list(map(int, input().split()))
    time = num[0] // num[1]
    if num[0] % num[1] > 0:
        print(num[2]*(time+1))
    else:
        print(num[2]*time)
resolve()