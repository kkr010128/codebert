H, A = map(int, input().split())

count = 0
while True:
    H -= A
    count += 1
    if H <= 0:
        print(count)
        exit()