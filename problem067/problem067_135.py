if __name__ == "__main__":
    n = int(input())
    taro, hanako = 0, 0
    for _ in range(n):
        tw, hw = input().split()
        if tw > hw:
            taro += 3
        elif tw < hw:
            hanako += 3
        else:
            taro += 1
            hanako += 1
    print(taro, hanako)