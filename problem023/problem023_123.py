if __name__ == '__main__':
    from collections import deque
    n = int(input())
    dic = {}

    for i in range(n):
        x = input().split()
        if x[0] == "insert":
            dic[x[1]] = 1
        if x[0] == "find":
            if x[1] in dic:
                print('yes')
            else:
                print('no')

