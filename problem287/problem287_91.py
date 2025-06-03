def solve():
    N = int(input())
    flag = False

    for i in range(9):
        for j in range(9):
            if((i+1)*(j+1) == N):
                print("Yes")
                flag = True
        if flag:
            break
    else:
        print("No")


if __name__ == "__main__":
    solve()
