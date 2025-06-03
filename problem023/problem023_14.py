N = int(input())
str_dict= {}

for i in range(N):
    a = input().split()
    if a[0] == "insert":
        str_dict[a[1]] = i
    else:
        if a[1] in str_dict.keys():
            print("yes")
        else:
            print("no")
