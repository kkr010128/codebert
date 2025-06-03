S = input()
P = input()
for i in range(len(S)):
    if P in S[i:] + S[:i]:
        print("Yes")
        exit()
print("No")
