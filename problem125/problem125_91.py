def main():
    X = int(input())
    tmp = 0
    cnt = 0
    while True:
        tmp += X
        cnt += 1
        tmp %= 360
        if tmp == 0:
            break
    return cnt 

print(main())
