import sys
alpha = "abcdefghijklmnopqrstuvwxyz"
cnt_dict = { key:0 for key in alpha}
string = sys.stdin.read().lower()
for i in alpha:
    print("{0} : {1}".format(i, string.count(i)))