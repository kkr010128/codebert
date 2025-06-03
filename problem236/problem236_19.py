H = int(input())
W = int(input())
N = int(input())
if N % max(H, W) == 0 :
    print(int(N / max(H, W)))
else :
    print(int(N / max(H, W)) + 1)
