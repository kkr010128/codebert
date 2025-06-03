n = int(input())
s = 'abcdefghijklmnopqrstuvwxyz'
ans = ''
while n > 0:
    n -= 1
#    print(n//26,n%26)
    ans = s[n%26] + ans
    n = n // 26
print(ans)