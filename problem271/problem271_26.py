alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n = int(input())
s = input()

ans = []
for i in range(len(s)):
    for j in range(len(alpha)):
        if s[i] == alpha[j]:
                ans.append(alpha[(j+n)%26])
print("".join(ans))