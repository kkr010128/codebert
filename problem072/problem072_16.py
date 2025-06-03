if __name__ == '__main__':
    try:
        count = []
        result = 0
        T = int(input())
        for _ in range(T):
            x, y = map(int, input().split())
            count.append([x, y])

        for i in range(T-2):
            if count[i][0] == count[i][1] and count[i+1][0] == count[i+1][1] and count[i+2][0] == count[i+2][1]:
                print("Yes")
                exit(0)

        print("No")
    except Exception:
        pass