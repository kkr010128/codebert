S,W=map(int,input().split())

if S<=W:
    print("unsafe")
elif S>W:
    print("safe")