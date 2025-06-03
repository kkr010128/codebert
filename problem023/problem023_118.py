import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    inp = sys.stdin.readlines()
    lis = set()
    for i in range(n):
        com = inp[i].split()
        if com[0] == "insert":
            lis.add(com[1])
        elif com[1] in lis:
            print("yes")
        else:
            print("no")