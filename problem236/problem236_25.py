H = int(input())
W = int(input())
N = int(input())

print(int(N/max(H,W)) + (1 if N % max(H,W) != 0 else 0))