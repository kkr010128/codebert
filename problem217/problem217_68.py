#155_B
n = int(input())
a = list(map(int, input().split()))

judge = True
for i in range(n):
    if a[i]%2 == 0:
        if a[i]%3 != 0 and a[i]%5 != 0:
            judge = False
            break

if judge:
    print('APPROVED')
else:
    print('DENIED')