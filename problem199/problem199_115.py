s = input()
n = len(s)
if n % 2 == 1:
    print("No")
    exit(0)
for i in range(n):
    if i % 2 == 0:
        if s[i] != "h":
            print("No")
            break
    elif s[i] != "i":
        print("No")
        break
else:
    print("Yes")
