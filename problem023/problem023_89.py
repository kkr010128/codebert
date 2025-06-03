from sys import stdin

def main():
    a = set()
    _ = int(stdin.readline())
    for command,value in (line.split() for line in stdin.readlines()):
        if command == "insert":
            a.add(value)
        else:
            print("yes" if value in a else "no")

main()
