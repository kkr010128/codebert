
s = list(input())
if len(s) % 2 != 0:
    print("No")
    exit()

while s:
    if s[0]=="h" and s[1] == "i":
        s.pop(0)
        s.pop(0)
    else:
        print("No")
        exit()

print("Yes")