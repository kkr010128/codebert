import sys

char_list = []
for line in sys.stdin:
    char_list.append([j for j in line.lower()])
char_dict = {i:0 for i in "abcdefghijklmnopqrstuvwxyz"}
for i in range(len(char_list)):
    for j in char_list[i]:
        if j in char_dict:
            char_dict[j] += 1
for i in char_dict:
    print(i+" : {0}".format(char_dict[i]))

