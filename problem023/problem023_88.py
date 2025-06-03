n = int(input())
index = set()

for _ in range(n):
    command, string = input().split()
    if command == "insert":
        index.add(string)
    else:
        if string in index:
            print("yes")
        else:
            print("no")
