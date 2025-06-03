while(1):
    H, W = map(int, input().split())
    if H==0 and W==0:
        break
    line = ""
    for w in range(W):
        line += "#"
    for h in range(H):
        print(line)
    print("")