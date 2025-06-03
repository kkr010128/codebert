R, G, B = map(int, input().split())
K = int(input())

cnt = 0

while not(R < G):
    G *= 2
    cnt += 1
while not(G < B):
    B *= 2
    cnt += 1

if cnt <= K:
    print('Yes')
else:
    print('No')