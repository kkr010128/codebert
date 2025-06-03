import string
n = int(input())
alphabet = list(string.ascii_lowercase)
ans = ''
while n > 0:
    ans = alphabet[(n-1) % 26] + ans
    n = (n-1) // 26
print(ans)
