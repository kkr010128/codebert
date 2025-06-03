while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    for n in range(a):
        mark1 = "#"
        mark2 = "."
        outLen = ""
        if n % 2 == 0 :
            mark1 = "."
            mark2 = "#"
        for m in range(b):
            if m % 2 != 0:
                outLen = outLen + mark1
            else:
                outLen = outLen + mark2
        print(outLen)
    print("")
