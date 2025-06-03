# B>G>R
R,G,B = map(int,input().split())
K = int(input())

cnt = 0

while not G>R:
    G *= 2
    cnt += 1

while not B>G:
    B *= 2
    cnt += 1
    
if cnt<=K:
    print("Yes")
else:
    print("No")