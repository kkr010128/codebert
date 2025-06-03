s = input()
n = int(input())
for i in range(n):
    tmp = input().split()
    a = int(tmp[1])
    b = int(tmp[2])
    if tmp[0] == "print":
        print(s[a:b+1])
    elif tmp[0] == "reverse":
        s = s[:a] + s[a:b+1][::-1] + s[b+1:]
    elif tmp[0] == "replace":
        s = s[:a] + tmp[3] + s[b+1:]
