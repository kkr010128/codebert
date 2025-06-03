import sys

num = map(int, raw_input().split())

if num[0] < num[1]:
    if num[1] < num[2]:
        print "Yes"
    else:
        print "No"
else:
    print "No"