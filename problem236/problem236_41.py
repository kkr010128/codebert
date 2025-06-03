from sys import stdin
H = int(stdin.readline().rstrip())
W = int(stdin.readline().rstrip())
N = int(stdin.readline().rstrip())
if N%(max(H,W))==0:
    print(N//(max(H,W)))
else:
    print(N//(max(H,W))+1)