n = int(input())
abc = 'abcdefghijklmnopqrstuvwxyz'
ans = ''
while n != 0:
    n -= 1
    ans += abc[n%26]
    n //= 26
print(ans[::-1])