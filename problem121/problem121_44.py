n = int(input())
str1 = ""

while n > 0:
    n -= 1
    m = n % 26
    n = n // 26
    str1 += chr(m+ord("a"))
ans = str1[::-1]
print(ans)