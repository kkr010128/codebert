n = int(input())
a = list(map(int, input().split()))

for i in a:
    if i % 2 == 0:
        if i % 6 > 0 and i % 10 > 0:
            print('DENIED')
            exit()
print('APPROVED')