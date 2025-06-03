from statistics import pstdev, variance, mean
while 1:
    num = int(input())
    if num == 0:
        break
    else:
        data = list(map(int, input().split()))
        st = float(pstdev(data))
        print(st)

