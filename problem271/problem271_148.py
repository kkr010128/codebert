alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet = list(alphabet)
n = int(input())
s = input()
l = len(s)
for i in range(l):
    k = alphabet.index(s[i])
    print(alphabet[(k+n)%26], end = "")
print()
