S = input()
T = input()
num = 0
length = len(S)
for i in range(length):
    if S[i] != T[i]:
        num += 1
print(num)