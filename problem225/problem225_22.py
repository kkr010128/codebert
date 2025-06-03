H,A = map(int,input().split())
cnt = 0
while True:
    if H <= 0:
        print(cnt)
        break
    else:
        H -= A
        cnt += 1
