s = input()
n = int(input())
for _ in range(n):
    in_s= input().split()
    command = str(in_s[0])
    a, b = int(in_s[1]), int(in_s[2])
    if(command == "print"):
        print(s[a:b+1])
    elif(command == "reverse"):
        s = s[:a] + s[a:b+1][::-1] + s[b+1:]
    else:
        p = str(in_s[3])
        s = s[:a] + p + s[b+1:]