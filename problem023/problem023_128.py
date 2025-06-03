def insert(string, hash_list):
    hali = hash_list
    if string not in hali:
        hali[string] = 1
    return hali


def find(string, hash_list):
    hali = hash_list
    return string in hali



n = int(input())
words = {}
operate = [list(input().split()) for i in range(n)]

for i in operate:
    if i[0] == "insert":
        insert(i[1], words)
    elif i[0] == "find":
        if find(i[1], words):
            print("yes")
        else:
            print("no")