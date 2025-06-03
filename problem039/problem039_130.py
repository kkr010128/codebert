inps = input().split()
if len(inps) >= 3:
    a = int(inps[0])
    b = int(inps[1])
    c = int(inps[2])
    if a < b and b < c:
        print("Yes")
    else:
        print("No")
else:
    print("Input illegal.")