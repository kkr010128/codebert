a, b = map(int,input().split())

cnt = 0

for i in range(1,1010):
    A = int(i * 8 //100)
    B = int(i * 10 //100)
    if (A == a) and (B == b):
        print(i)
        cnt += 1
        break

if cnt == 0:
    print(-1)