while True:
    n = list(map(int,input().split()))
    if(n[0] == n[1] == 0):break
    print(" ".join(map(str,sorted(n))))