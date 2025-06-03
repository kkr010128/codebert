N = int(input())

chars = "Xabcdefghijklmnopqrstuvwxyz"
result = ""
n_1 = N

while True:
    x = n_1 % 26

    if x == 0:
        x = 26

    result += chars[x]
    n_1 -= x
    if n_1 == 0:
        break

    n_1 //= 26

print(result[::-1])

