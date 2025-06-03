values = input()
a, b, c = [int(x) for x in values.split()]
cnt = 0
for i in range(a, b + 1):
    if 0 == c % i:
        cnt += 1

print(cnt)