N = int(input())
C = [list(map(int, input().split())) for _ in range(N)]

counter = 0
for d1, d2 in C:
    if d1 == d2:
        counter += 1
    else:
        counter = 0

    if counter == 3:
        print('Yes')
        exit()
print('No')
