import sys
n = int(input())
command = sys.stdin.readlines()
Q = {}
for i in range(n):
    a,b = command[i].split()
    if a == "insert":
        Q[b] = 0
    else:
        if b in Q.keys():
            print("yes")
        else:
            print("no")