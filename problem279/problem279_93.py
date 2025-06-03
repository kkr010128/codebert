n = int(input())
s = input()

t1 = s[:n//2]
t2 = s[n//2:n]

if(t1 == t2):
    print("Yes")
else:
    print("No")

