x = int(input())
b,cnt = 100, 0

while True:
    a = b
    b = b + a // 100
    cnt += 1
    if b >= x:
        break

print(cnt)
