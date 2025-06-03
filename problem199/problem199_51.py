s = input()

if len(s)%2!=0:
    print("No")
else:
    if s.count("hi") == len(s)//2:
        print("Yes")
    else:
        print("No")