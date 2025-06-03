while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break;
    for i in range(0, a):
        if i % 2 == 0:
            print(("#." * int((b + 1) / 2))[:b])
        else:
            print((".#" * int((b + 1) / 2))[:b])
    print("")