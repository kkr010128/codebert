n = int(input())
s = input()
if n % 2 != 0:
    print("No")
else:
    t = s[:int((n / 2))]
    u = t + t
    print("Yes" if s == u else "No")