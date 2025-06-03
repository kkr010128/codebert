H = int(input())

cnt = 0

while True:
    H //= 2
    cnt += 1

    if H == 0:
        break

print(2**cnt-1)

