H,A = map(int,input().split())

t = 0
for i in range(H):
    H -= A
    t += 1
    if H<=0:
        print(t)
        exit()