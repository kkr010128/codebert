n = int(input())

flg = False
for i in range(1, 10):
    if n % i == 0 and 1 <= n // i < 10:
        flg = True
        break
print('Yes') if flg else print('No')