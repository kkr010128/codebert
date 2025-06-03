def some():
    n = int(input())
    for i in range(9, 0, -1):
        for j in range(9, 0, -1):
            if i* j == n:
                print("Yes")
                exit()
    print("No")

some()