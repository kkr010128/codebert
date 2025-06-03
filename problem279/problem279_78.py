n = int(input())
s = input()
if len(s) % 2 == 0:
    if s[:int(n/2)] == s[int(n/2):]:
        print("Yes")
    else:
        print("No")
else:
    print("No")