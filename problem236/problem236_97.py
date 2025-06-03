import sys
H = int(sys.stdin.readline())
W = int(sys.stdin.readline())
N = int(sys.stdin.readline())
 
print((N - 1) // max(H, W) + 1)