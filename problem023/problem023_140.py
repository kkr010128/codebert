n = int(input())
dictionary = {}
for i in range(n):
    a = input().split()
    if a[0] == "insert":
        dictionary[a[1]] = 0
    if a[0] == "find":
        if a[1] in dictionary:
            print("yes")
        else:
            print("no") 