n = int(input())
if n % 2 == 1:
    print(0)
    exit(0)
cnt = 0
five = 2 * 5
while n // five > 0:
    cnt += n // five
    five *= 5
print(cnt)