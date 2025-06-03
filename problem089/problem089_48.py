import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
H, W, M = map(int, readline().split())
bomb = [tuple(map(lambda x: int(x) - 1, s.split())) for s in readlines()]
X = [0] * H 
Y = [0] * W 
for h, w in bomb:
    X[h] += 1
    Y[w] += 1
maxX = max(X)
maxY = max(Y)

R = [h for h, x in enumerate(X) if x == maxX]  
C = [w for w, y in enumerate(Y) if y == maxY] 

bomb = set(bomb)
for r in R:
    for c in C:
        if (r, c) not in bomb:
            print(maxX + maxY)
            exit()
print(maxX + maxY - 1)