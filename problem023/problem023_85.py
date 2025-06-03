n = input()
dictInProb = set()
for i in range(int(n)):
    cmdAndStr = list(input().split())
    if cmdAndStr[0] == "insert":
        dictInProb.add(cmdAndStr[1])
    elif cmdAndStr[0] == "find":
        if cmdAndStr[1] in dictInProb:
            print("yes")
        else:
            print("no")
    else: pass