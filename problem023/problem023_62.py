n= int(input())
s= set()
for _ in range(n):
    a,b= input().split()
    if a=="insert":
        s.add(b)
    elif b in s:
        print("yes")
    else:
        print("no")

