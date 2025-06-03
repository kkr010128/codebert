s = input()

if len(s) % 2 == 1:
    print("No")
    exit()

for i in range(0, len(s)-1, 2):
    if s[i] + s[i+1] != "hi":
        print("No")
        exit()

print("Yes")
