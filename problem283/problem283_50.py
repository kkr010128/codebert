N = int(input())

if N % 2 == 0:
    ans = int(N / 2) - 1
else:
    ans = int(N / 2)

print('{}'.format(ans))

