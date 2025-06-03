N = int(input())

if N % 2 == 1:
    print(0)
    exit()

res = 0
fives = 10
while True:
    if N // fives == 0:
        break
    res += N//fives
    fives *= 5
print(res)