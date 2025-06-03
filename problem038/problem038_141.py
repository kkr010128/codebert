inps = input().split()
if len(inps) >= 2:
    a = int(inps[0])
    b = int(inps[1])
    if a > b:
        print("a > b")
    elif a < b:
        print("a < b")
    else:
        print("a == b")
else:
    print("Input illegal.")