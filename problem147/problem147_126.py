s=input()
t=input()

if len(s)+1 == len(t):
    if s==t[:len(s)]:
        print("Yes")
        exit()

print("No")