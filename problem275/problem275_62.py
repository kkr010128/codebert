def resolve():
    X, Y = input().split()
    ans = 0
    if X == "3":
        ans += 100000
    elif X == "2":
        ans += 200000
    elif X == "1":
        ans += 300000
    else:
        ans += 0
    if Y == "3":
        ans += 100000
    elif Y == "2":
        ans += 200000
    elif Y == "1":
        ans += 300000
    else:
        ans += 0
    if X == "1" and Y == "1":
        ans += 400000
    else:
        ans += 0
    print(ans)
resolve()