N = int(input())
ans = ""
letter = "abcdefghijklmnopqrstuvwxyz"

while N != 0:
    N -= 1
    ans = letter[N % 26] + ans
    N = N // 26
print(ans)
