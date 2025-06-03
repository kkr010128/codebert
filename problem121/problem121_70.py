a = ''
n = int(input())
while n> 0:
    n -= 1
    a += chr(ord('a') + n%26)
    n //=26
print(a[::-1])
