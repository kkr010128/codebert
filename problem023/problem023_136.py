
n = int(input())
dic = set()

for i in range(n):
    cmd = input().split()

    if cmd[0] == "insert":
        dic.add(cmd[1])
    else:
        print("yes" if cmd[1] in dic else "no")