#-*-coding:utf-8-*-

from collections import deque
import sys
input=sys.stdin.readline

def main():
    commands=[]
    number = int(input())
    commands=list(input().split() for _ in range(number))
    q=deque()
    for command in commands:
        if command[0] == "insert":
            q.appendleft(command[1])
        elif command[0] == "delete":
            if command[1] in q:
                q.remove(command[1])
            else:
                continue
        elif command[0] == "deleteFirst":
            q.popleft()
        elif command[0] == "deleteLast":
            q.pop()
    print(*q)
if __name__=="__main__":
    main()
