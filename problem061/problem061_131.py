line = input()

for ch in line:
    n = ord(ch)

    if   ord('a') <= n <= ord('z'):
        n -= 32
    elif ord('A') <= n <= ord('Z'):
        n += 32

    print(chr(n), end='')

print()