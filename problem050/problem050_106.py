while True:
    a, b = map(int, input().split())
    if(a == 0 and b == 0):
        break
    for i in range(a):
        for j in range(b):
            if(0 < i < a-1 and 0 < j < b-1):
                print(".", end = "")
            else:
                print("#", end = "")
        print()
    print()
