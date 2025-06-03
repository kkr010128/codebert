n = int(input())
s = input()
h = int(n/2)
s=list(s)
if s[0:h] == s[h:n]:
    print("Yes")
else: print("No")