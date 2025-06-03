import sys

p = 0
for line in sys.stdin:
    ls = line.strip('\n')
    if p == 0:
        if ls =='-': break
        letters = ls
        p = 1
    elif p == 1:
        m = int(ls)
        p =2
    elif p == 2:
        h = int(ls)
        letters = letters[h:] + letters[:h]
        if m > 1:
            m -= 1
        else:
            print letters
            p = 0