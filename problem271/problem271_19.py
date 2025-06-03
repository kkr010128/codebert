N = int(input())
S = input()

ans = ""
for i in range(len(S)):
    ord_c = ord(S[i])
    # print(chr((ord_c + N - 65) % 26 + 65))
    ans += chr((ord_c + N - 65) % 26 + 65)
print(ans)
