def solve():
    N = int(input())
    aList = [list(input().split()) for i in range(N)]
    X = input()

    sleep = False
    ans = 0

    for item in aList:
        if sleep == True:
            ans += int(item[1])
        if X == item[0]:
            sleep = True

    print(ans)
    
if __name__ == '__main__':
    solve()
