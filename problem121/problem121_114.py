import string

n = int(input())
s = ''
lowCase = string.ascii_lowercase

while n > 0:
    n -= 1
    s += lowCase[int(n % 26)]
    n //= 26

print(s[::-1])
