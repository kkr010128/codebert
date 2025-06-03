N = int(input())
S = input()
list = []
for i in range(len(S)):
    a = ord(S[i]) + N
    if a > 90:
        a -= 26
    list.append(chr(a))
print("".join(list))