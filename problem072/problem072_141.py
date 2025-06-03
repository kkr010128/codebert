n = int(input())
answer = 0
for i in range(n):
    x, y = input().split()
    if x == y:
        answer = answer + 1
    else:
        answer = 0
    if answer == 3:
        print('Yes')
        exit(0)
else:
    print('No')
