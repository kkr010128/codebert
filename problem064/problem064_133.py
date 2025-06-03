s = input()
p = input()

s = s * 2

for i in range(len(s) - len(p) + 1):
    #print(s[i:i + len(p)])
    if p == s[i:i + len(p)]:
        print("Yes")
        exit()

print("No")
