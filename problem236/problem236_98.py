H = int(input())
W = int(input())
N = int(input())
for i in range(min(H,W)):
    N -= max(H, W)
    if N <= 0:
        print(i+1)
        exit()