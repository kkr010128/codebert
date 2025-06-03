flag = "go"
cnt = 0
while flag == "go":
    cnt += 1
    x = int(input())
    if x == 0:
        flag = "stop"
    else:
        print("Case " + str(cnt) + ": " + str(x))
