n = int(input())
s = input()

if n % 2 == 1:
    print("No")
else:
    t = s[:n//2]
    if t * 2 == s:
        print("Yes")
    else:
        print("No")