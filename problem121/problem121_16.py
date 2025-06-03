N = int(input())

# 26進数に変換する問題
ans = ""
alphabet = "Xabcdefghijklmnopqrstuvwxyz"
while N > 0:
    mod = N % 26
    if mod == 0:
        mod = 26
    ans = alphabet[mod] + ans
    N -= mod
    N //= 26

print(ans)
