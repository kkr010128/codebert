n = int(input())
s = input()
t = s[:len(s)//2]
if 2*t == s:
    print("Yes")
else:
    print("No")