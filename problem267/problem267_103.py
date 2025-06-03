def main():
    n = int(input())
    T = tuple(map(int, input()))
    ans = 0
    for i in range(0, 1000):
        a = i // 100
        b = (i // 10) % 10
        c = i % 10
        flag1 = False
        flag2 = False
        flag3 = False
        for t in T:
            if flag2:
                if t == c:
                    flag3 = True
                    break
            if flag1:
                if t == b:
                    flag2 = True
                    continue
            if t == a:
                flag1 = True

        if flag3:
            ans += 1
    print(ans)
if __name__ == "__main__":
    main()