alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n = int(input())
s = input()
for c in s:
    for i in range(26):
        if alphabet[i] == c:
            print(alphabet[(i + n) % 26], end="")
print("")

