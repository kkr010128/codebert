import sys

dic = {}
for i in range(ord('a'), ord('z') + 1):
    dic[chr(i)] = 0

for line in sys.stdin:
    for i in range(len(line)):
        char = line[i].lower()
        if char in dic.keys():dic[char] += 1

for i in range(ord('a'), ord('z') + 1):
    print("{} : {}".format(chr(i), dic[chr(i)]))