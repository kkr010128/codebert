import sys


inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inintm())
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())

n, m = inintm()

if n == 1:
    if m == 0:
        print(0)
        exit()
    ans = "0"
    s, c = inintm()
    ans = str(c)
    for i in range(m-1):
        s, c = inintm()
        if ans != str(c):
            print(-1)
            exit()
    print(ans)
elif n == 2:
    if m == 0:
        print(10)
        exit()
    ans = ["0","0"]
    flag = ["0","0"]
    for i in range(m):
        s, c = inintm()
        if flag[s-1] == "1":
            if str(c) != ans[s-1]:
                print(-1)
                exit()
        flag[s-1] = "1"
        ans[s-1] = str(c)
    if ans[0] == "0":
        if flag[0] == "1":
            print(-1)
            exit()
        else:
            ans[0] = "1"
    print("".join(ans))
else:
    if m == 0:
        print(100)
        exit()
    ans = ["0","0","0"]
    flag = ["0","0","0"]
    for i in range(m):
        s, c = inintm()
        if flag[s-1] == "1":
            if str(c) != ans[s-1]:
                print(-1)
                exit()
        flag[s-1] = "1"
        ans[s-1] = str(c)
    if ans[0] == "0":
        if flag[0] == "1":
            print(-1)
            exit()
        else:
            ans[0] = "1"
    print("".join(ans))
