n=int(input())
s=input()
t=""
for i in range(len(s)//2):
    t += s[i]

if s == t + t:
    print("Yes")
else:
    print("No")