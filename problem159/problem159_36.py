def main():
    X = int(input())
    cnt = 0
    money = 100
    while money < X:
        cnt += 1
        money = money * 101
        money //= 100
        #print(money)

    return cnt

print(main())
