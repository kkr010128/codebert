a, b = list(map(int, input().split()))

if a < b:
    a, b = b, a


while True:
    if b == 0:
        break
    tmp = a % b
    a = b
    b = tmp

print(a)

