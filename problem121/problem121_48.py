n = int(input())

ans = ''

for i in range(13):
    if n >= 26 and n%26 == 0:
        ans = 'z' + ans
        n -= 26
    else:
        ans = chr(97 -1 + n%26) + ans
        n -= n%26

    n = n //26

print(ans.replace("`", ""))
